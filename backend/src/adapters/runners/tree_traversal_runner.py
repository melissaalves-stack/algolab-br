# BFS (Busca em Largura) em uma árvore binária.
# Percorre nível por nível usando uma fila (deque).
# Input: dicionário representando a árvore. Exemplo:
#   {"value": 1, "left": {"value": 2, ...}, "right": {"value": 3, ...}}

from collections import deque
from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class BFSTreeRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        steps: list[ExecutionStep] = []
        step_num = 0
        visited_order: list = []

        # A fila começa com a raiz. Cada item é (nó, id único para highlight)
        queue: deque = deque()
        queue.append((input_data, "root"))

        while queue:
            node, node_id = queue.popleft()
            visited_order.append(node["value"])

            steps.append(ExecutionStep(
                step_number=step_num,
                description=f"Visitando nó {node['value']}. Ordem até agora: {visited_order}",
                state={"tree": input_data, "visited": list(visited_order), "current": node["value"]},
                highlighted=[node["value"]],
            ))
            step_num += 1

            # Adiciona filhos à fila (da esquerda para a direita = ordem de nível)
            if node.get("left"):
                queue.append((node["left"], f"{node_id}-left"))
            if node.get("right"):
                queue.append((node["right"], f"{node_id}-right"))

        steps.append(ExecutionStep(
            step_number=step_num,
            description=f"BFS completo! Ordem de visita: {visited_order}",
            state={"tree": input_data, "visited": visited_order},
            highlighted=[],
            is_final=True,
        ))
        return steps
