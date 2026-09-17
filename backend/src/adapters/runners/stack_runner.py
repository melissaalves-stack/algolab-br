# Pilha (Stack): estrutura LIFO — Last In, First Out (último a entrar, primeiro a sair).
# Pense numa pilha de pratos: você sempre coloca e tira do topo.
# Input: lista de operações. Ex: [{"op": "push", "value": 5}, {"op": "pop"}]

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class StackRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        stack: list = []
        steps: list[ExecutionStep] = []
        step_num = 0

        for operation in input_data:
            op = operation.get("op")
            value = operation.get("value")

            if op == "push":
                stack.append(value)
                steps.append(ExecutionStep(
                    step_number=step_num,
                    description=f"PUSH {value}: empilhado no topo. Pilha agora tem {len(stack)} elemento(s).",
                    state={"stack": list(stack), "operation": "push", "value": value, "top": len(stack) - 1},
                    highlighted=[len(stack) - 1],
                ))

            elif op == "pop":
                if not stack:
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description="POP: pilha vazia! Não há nada para remover (underflow).",
                        state={"stack": [], "operation": "pop_error"},
                        highlighted=[],
                    ))
                else:
                    removed = stack.pop()
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description=f"POP: removido {removed} do topo. Pilha agora tem {len(stack)} elemento(s).",
                        state={"stack": list(stack), "operation": "pop", "removed": removed},
                        highlighted=[],
                    ))

            elif op == "peek":
                if stack:
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description=f"PEEK: topo é {stack[-1]} (sem remover).",
                        state={"stack": list(stack), "operation": "peek", "top_value": stack[-1]},
                        highlighted=[len(stack) - 1],
                    ))

            step_num += 1

        steps.append(ExecutionStep(
            step_number=step_num,
            description=f"Operações concluídas. Estado final da pilha: {stack}",
            state={"stack": list(stack)},
            highlighted=[],
            is_final=True,
        ))
        return steps
