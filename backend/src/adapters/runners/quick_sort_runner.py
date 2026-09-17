# Quick Sort: escolhe um pivô, coloca todos os menores à esquerda e maiores à direita,
# depois repete recursivamente em cada lado. Na média é O(n log n).

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class QuickSortRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        arr = input_data.copy()
        steps: list[ExecutionStep] = []
        counter = [0]
        self._quick_sort(arr, 0, len(arr) - 1, steps, counter)
        steps.append(ExecutionStep(
            step_number=counter[0],
            description="Array ordenado pelo Quick Sort!",
            state={"array": arr.copy()},
            highlighted=[],
            is_final=True,
        ))
        return steps

    def _quick_sort(self, arr, low, high, steps, counter):
        if low >= high:
            return
        pivot_idx = self._partition(arr, low, high, steps, counter)
        self._quick_sort(arr, low, pivot_idx - 1, steps, counter)
        self._quick_sort(arr, pivot_idx + 1, high, steps, counter)

    def _partition(self, arr, low, high, steps, counter):
        pivot = arr[high]  # escolhe o último elemento como pivô
        i = low - 1        # i aponta para o último elemento menor que o pivô

        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Pivô escolhido: {pivot} (índice {high}). Particionando {low}..{high}",
            state={"array": arr.copy(), "pivot": pivot, "low": low, "high": high},
            highlighted=[high],
        ))
        counter[0] += 1

        for j in range(low, high):
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Comparando arr[{j}]={arr[j]} com pivô {pivot}",
                state={"array": arr.copy(), "pivot_index": high},
                highlighted=[j, high],
            ))
            counter[0] += 1

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                if i != j:
                    steps.append(ExecutionStep(
                        step_number=counter[0],
                        description=f"Trocando arr[{i}]={arr[j]} com arr[{j}]={arr[i]}",
                        state={"array": arr.copy()},
                        highlighted=[i, j],
                    ))
                    counter[0] += 1

        # Coloca o pivô na posição correta
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Pivô {pivot} na posição final: índice {i+1}",
            state={"array": arr.copy(), "pivot_final": i + 1},
            highlighted=[i + 1],
        ))
        counter[0] += 1
        return i + 1
