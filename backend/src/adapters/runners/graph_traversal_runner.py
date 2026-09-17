# DFS (Busca em Profundidade) em um grafo representado como lista de adjacência.
# Usa uma pilha (lista Python) em vez de recursão para evitar stack overflow.
# Input: {"graph": {"A": ["B", "C"], "B": ["D"], ...}, "start": "A"}

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class DFSGraphRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        graph: dict[str, list[str]] = input_data["graph"]
        start: str = input_data["start"]
        steps: list[ExecutionStep] = []
        step_num = 0

        visited: set[str] = set()
        stack: list[str] = [start]
        visit_order: list[str] = []

        while stack:
            node = stack.pop()  # tira o último elemento (topo da pilha)

            if node in visited:
                continue  # já visitado, pula

            visited.add(node)
            visit_order.append(node)

            steps.append(ExecutionStep(
                step_number=step_num,
                description=f"Visitando '{node}'. Pilha: {stack}. Ordem: {visit_order}",
                state={
                    "graph": graph,
                    "visited": list(visited),
                    "stack": list(stack),
                    "visit_order": list(visit_order),
                    "current": node,
                },
                highlighted=[node],
            ))
            step_num += 1

            # Adiciona vizinhos não visitados à pilha (invertido para manter ordem alfabética)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

        steps.append(ExecutionStep(
            step_number=step_num,
            description=f"DFS completo! Ordem de visita: {visit_order}",
            state={"graph": graph, "visit_order": visit_order},
            highlighted=[],
            is_final=True,
        ))
        return steps
