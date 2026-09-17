# DFS em Árvore: percorre em profundidade, descendo até a folha antes de voltar.
# Três variações: pré-ordem (raiz, esq, dir), in-ordem (esq, raiz, dir), pós-ordem (esq, dir, raiz).
# Input: {"tree": {...}, "order": "pre"/"in"/"post"}

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class DFSTreeRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        tree = input_data.get("tree")
        order = input_data.get("order", "pre")
        steps: list[ExecutionStep] = []
        counter = [0]
        visited: list = []

        order_names = {"pre": "Pré-ordem (raiz → esquerda → direita)", "in": "In-ordem (esquerda → raiz → direita)", "post": "Pós-ordem (esquerda → direita → raiz)"}
        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"Iniciando DFS {order_names.get(order, order)} na árvore.",
            state={"tree": tree, "visited": []},
            highlighted=[],
        ))
        counter[0] += 1

        self._dfs(tree, order, steps, counter, visited)

        steps.append(ExecutionStep(
            step_number=counter[0],
            description=f"DFS completo! Ordem de visita ({order}): {visited}",
            state={"tree": tree, "visited": list(visited)},
            highlighted=[],
            is_final=True,
        ))
        return steps

    def _dfs(self, node, order, steps, counter, visited):
        if node is None:
            return

        if order == "pre":
            visited.append(node["value"])
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Pré-ordem: visitando raiz {node['value']}. Ordem até agora: {visited}",
                state={"tree": node, "visited": list(visited), "current": node["value"]},
                highlighted=[node["value"]],
            ))
            counter[0] += 1
            self._dfs(node.get("left"), order, steps, counter, visited)
            self._dfs(node.get("right"), order, steps, counter, visited)

        elif order == "in":
            self._dfs(node.get("left"), order, steps, counter, visited)
            visited.append(node["value"])
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"In-ordem: visitando {node['value']} (entre esquerda e direita). Ordem: {visited}",
                state={"tree": node, "visited": list(visited), "current": node["value"]},
                highlighted=[node["value"]],
            ))
            counter[0] += 1
            self._dfs(node.get("right"), order, steps, counter, visited)

        elif order == "post":
            self._dfs(node.get("left"), order, steps, counter, visited)
            self._dfs(node.get("right"), order, steps, counter, visited)
            visited.append(node["value"])
            steps.append(ExecutionStep(
                step_number=counter[0],
                description=f"Pós-ordem: visitando {node['value']} (após filhos). Ordem: {visited}",
                state={"tree": node, "visited": list(visited), "current": node["value"]},
                highlighted=[node["value"]],
            ))
            counter[0] += 1
