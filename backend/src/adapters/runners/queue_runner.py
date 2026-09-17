# Fila (Queue): estrutura FIFO — First In, First Out (primeiro a entrar, primeiro a sair).
# Pense numa fila de banco: quem chega primeiro é atendido primeiro.
# Input: lista de operações. Ex: [{"op": "enqueue", "value": 5}, {"op": "dequeue"}]

from collections import deque
from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class QueueRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        queue: deque = deque()
        steps: list[ExecutionStep] = []
        step_num = 0

        for operation in input_data:
            op = operation.get("op")
            value = operation.get("value")

            if op == "enqueue":
                queue.append(value)
                steps.append(ExecutionStep(
                    step_number=step_num,
                    description=f"ENQUEUE {value}: adicionado ao final da fila. Tamanho: {len(queue)}.",
                    state={"queue": list(queue), "operation": "enqueue", "value": value, "back": len(queue) - 1},
                    highlighted=[len(queue) - 1],
                ))

            elif op == "dequeue":
                if not queue:
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description="DEQUEUE: fila vazia! Não há nada para remover (underflow).",
                        state={"queue": [], "operation": "dequeue_error"},
                        highlighted=[],
                    ))
                else:
                    removed = queue.popleft()
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description=f"DEQUEUE: removido {removed} da frente. Tamanho: {len(queue)}.",
                        state={"queue": list(queue), "operation": "dequeue", "removed": removed},
                        highlighted=[],
                    ))

            elif op == "peek":
                if queue:
                    steps.append(ExecutionStep(
                        step_number=step_num,
                        description=f"PEEK: frente da fila é {queue[0]} (sem remover).",
                        state={"queue": list(queue), "operation": "peek", "front_value": queue[0]},
                        highlighted=[0],
                    ))

            step_num += 1

        steps.append(ExecutionStep(
            step_number=step_num,
            description=f"Operações concluídas. Estado final da fila: {list(queue)}",
            state={"queue": list(queue)},
            highlighted=[],
            is_final=True,
        ))
        return steps
