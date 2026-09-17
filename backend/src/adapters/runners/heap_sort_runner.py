# Heap Sort: primeiro transforma o array em um max-heap (árvore onde o pai é sempre maior
# que os filhos), depois extrai o maior elemento repetidamente para ordenar.

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class HeapSortRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        arr = input_data.copy()
        n = len(arr)
        steps: list[ExecutionStep] = []
        counter = [0]

        # Fase 1: constrói o max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i, steps, counter)

        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Max-heap construído: {arr}. Agora vamos extrair o maior elemento repetidamente.",
            state={"array": arr.copy()},
            highlighted=list(range(n)),
        ))
        counter[0] += 1

        # Fase 2: extrai o maior (raiz) e reorganiza
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Maior elemento ({arr[i]}) movido para índice {i}",
                state={"array": arr.copy(), "sorted_from": i},
                highlighted=[0, i],
            ))
            counter[0] += 1
            self._heapify(arr, i, 0, steps, counter)

        steps.append(ExecutionStep(
            step_number=counter[0],
            description="Array ordenado pelo Heap Sort!",
            state={"array": arr.copy()},
            highlighted=[],
            is_final=True,
        ))
        return steps

    def _heapify(self, arr, n, i, steps, counter):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Heapify: trocando arr[{i}]={arr[largest]} com arr[{largest}]={arr[i]}",
                state={"array": arr.copy()},
                highlighted=[i, largest],
            ))
            counter[0] += 1
            self._heapify(arr, n, largest, steps, counter)
