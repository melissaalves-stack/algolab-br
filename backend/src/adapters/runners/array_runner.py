# Implementação concreta do Bubble Sort.
# Herda de AlgorithmRunner e implementa run().
# A cada troca ou comparação, registra um ExecutionStep com o estado atual do array.

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class BubbleSortRunner(AlgorithmRunner):

    def run(self, input_data: list[int]) -> list[ExecutionStep]:
        arr = input_data.copy()  # nunca muda o input original
        steps: list[ExecutionStep] = []
        n = len(arr)
        step_num = 0

        for i in range(n):
            for j in range(0, n - i - 1):
                # Registra o passo de comparação antes de qualquer troca
                steps.append(ExecutionStep(
                    step_number=step_num,
                    description=f"Comparando arr[{j}]={arr[j]} com arr[{j+1}]={arr[j+1]}",
                    state={"array": arr.copy()},
                    highlighted=[j, j + 1],
                ))
                step_num += 1

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description=f"Trocando {arr[j+1]} e {arr[j]}",  # valores já trocados
                        state={"array": arr.copy()},
                        highlighted=[j, j + 1],
                    ))
                    step_num += 1

        # Passo final com array ordenado, sem nada destacado
        steps.append(ExecutionStep(
            step_number=step_num,
            description="Array ordenado!",
            state={"array": arr.copy()},
            highlighted=[],
            is_final=True,
        ))
        return steps
