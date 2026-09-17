# Binary Search: divide o array ao meio a cada passo.
# O input_data precisa ser um dict com "array" (ordenado) e "target" (o que procurar).

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class BinarySearchRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        arr: list[int] = input_data["array"]
        target: int = input_data["target"]
        steps: list[ExecutionStep] = []
        step_num = 0

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            steps.append(ExecutionStep(
                step_number=step_num,
                description=f"Meio em índice {mid} (valor {arr[mid]}). left={left}, right={right}",
                state={"array": arr, "left": left, "right": right, "mid": mid},
                highlighted=[mid],
            ))
            step_num += 1

            if arr[mid] == target:
                steps.append(ExecutionStep(
                    step_number=step_num,
                    description=f"Encontrado! {target} está no índice {mid}.",
                    state={"array": arr, "found_index": mid},
                    highlighted=[mid],
                    is_final=True,
                ))
                return steps

            elif arr[mid] < target:
                # Alvo está na metade direita
                left = mid + 1
            else:
                # Alvo está na metade esquerda
                right = mid - 1

        steps.append(ExecutionStep(
            step_number=step_num,
            description=f"{target} não está no array.",
            state={"array": arr, "found_index": -1},
            highlighted=[],
            is_final=True,
        ))
        return steps
