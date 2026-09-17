# Merge Sort: divide o array ao meio recursivamente, depois mescla as metades ordenadas.
# É um algoritmo clássico de divisão e conquista — muito mais eficiente que o Bubble Sort.

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class MergeSortRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        arr = input_data.copy()
        steps: list[ExecutionStep] = []
        self._merge_sort(arr, 0, len(arr) - 1, steps, [0])
        steps.append(ExecutionStep(
            step_number=len(steps),
            description="Array completamente ordenado pelo Merge Sort!",
            state={"array": arr.copy()},
            highlighted=[],
            is_final=True,
        ))
        return steps

    def _merge_sort(self, arr, left, right, steps, counter):
        if left >= right:
            return
        mid = (left + right) // 2

        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Dividindo: índices {left}..{mid} e {mid+1}..{right}",
            state={"array": arr.copy(), "left": left, "right": right, "mid": mid},
            highlighted=list(range(left, right + 1)),
        ))
        counter[0] += 1

        self._merge_sort(arr, left, mid, steps, counter)
        self._merge_sort(arr, mid + 1, right, steps, counter)
        self._merge(arr, left, mid, right, steps, counter)

    def _merge(self, arr, left, mid, right, steps, counter):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Comparando {left_part[i]} (esquerda) com {right_part[j]} (direita)",
                state={"array": arr.copy()},
                highlighted=[left + i, mid + 1 + j],
            ))
            counter[0] += 1

            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Mesclando índices {left}..{right} → {arr[left:right+1]}",
            state={"array": arr.copy()},
            highlighted=list(range(left, right + 1)),
        ))
        counter[0] += 1
