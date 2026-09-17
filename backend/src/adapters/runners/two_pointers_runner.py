# Two Pointers: encontra dois números em um array ordenado que somam ao target.
# Um ponteiro começa no início, o outro no fim. Eles se aproximam até se encontrarem.
# Input: {"array": [...], "target": N}

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class TwoPointersRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        arr: list[int] = input_data["array"]
        target: int = input_data["target"]
        steps: list[ExecutionStep] = []
        step_num = 0

        left, right = 0, len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            steps.append(ExecutionStep(
                step_number=step_num,
                description=f"arr[{left}]={arr[left]} + arr[{right}]={arr[right]} = {current_sum}",
                state={"array": arr, "left": left, "right": right, "sum": current_sum},
                highlighted=[left, right],
            ))
            step_num += 1

            if current_sum == target:
                steps.append(ExecutionStep(
                    step_number=step_num,
                    description=f"Par encontrado: índices {left} e {right}!",
                    state={"array": arr, "result": [left, right]},
                    highlighted=[left, right],
                    is_final=True,
                ))
                return steps
            elif current_sum < target:
                left += 1   # soma muito baixa: avança o ponteiro da esquerda
            else:
                right -= 1  # soma muito alta: recua o ponteiro da direita

        steps.append(ExecutionStep(
            step_number=step_num,
            description="Nenhum par encontrado.",
            state={"array": arr, "result": []},
            highlighted=[],
            is_final=True,
        ))
        return steps
