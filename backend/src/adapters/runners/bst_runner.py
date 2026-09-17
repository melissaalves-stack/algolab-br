# BST (Árvore Binária de Busca): cada nó tem no máximo dois filhos.
# Regra: tudo à esquerda é menor, tudo à direita é maior.
# Isso permite buscas em O(log n) em árvores balanceadas.
# Input: {"operations": [{"op": "insert", "value": 5}, {"op": "search", "value": 3}]}

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_to_dict(node):
    # Converte a árvore em dicionário para serializar como JSON
    if node is None:
        return None
    return {"value": node.value, "left": tree_to_dict(node.left), "right": tree_to_dict(node.right)}


class BSTRunner(AlgorithmRunner):

    def run(self, input_data: dict) -> list[ExecutionStep]:
        operations = input_data.get("operations", [])
        steps: list[ExecutionStep] = []
        step_num = 0
        root: BSTNode | None = None

        for operation in operations:
            op = operation.get("op")
            value = operation.get("value")

            if op == "insert":
                root, insert_steps = self._insert(root, value, step_num)
                for s in insert_steps:
                    steps.append(s)
                step_num += len(insert_steps)

            elif op == "search":
                search_steps = self._search(root, value, step_num)
                for s in search_steps:
                    steps.append(s)
                step_num += len(search_steps)

        steps.append(ExecutionStep(
            step_number=step_num,
            description="Operações na BST concluídas.",
            state={"tree": tree_to_dict(root)},
            highlighted=[],
            is_final=True,
        ))
        return steps

    def _insert(self, node, value, start_step):
        steps = []
        path = []

        def _do_insert(current, val):
            if current is None:
                new_node = BSTNode(val)
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Inserindo {val}: posição encontrada! Nó criado.",
                    state={"tree": tree_to_dict(root_ref[0])},
                    highlighted=[val],
                ))
                return new_node
            path.append(current.value)
            if val < current.value:
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Inserindo {val}: {val} < {current.value}, vai para a esquerda. Caminho: {path}",
                    state={"tree": tree_to_dict(root_ref[0])},
                    highlighted=[current.value],
                ))
                current.left = _do_insert(current.left, val)
            else:
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Inserindo {val}: {val} >= {current.value}, vai para a direita. Caminho: {path}",
                    state={"tree": tree_to_dict(root_ref[0])},
                    highlighted=[current.value],
                ))
                current.right = _do_insert(current.right, val)
            return current

        root_ref = [node]
        result = _do_insert(node, value)
        if node is None:
            root_ref[0] = result
        return result, steps

    def _search(self, root, value, start_step):
        steps = []
        current = root
        path = []

        while current:
            path.append(current.value)
            if current.value == value:
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Buscando {value}: ENCONTRADO no nó {current.value}! Caminho percorrido: {path}",
                    state={"tree": tree_to_dict(root), "found": value},
                    highlighted=[value],
                ))
                return steps
            elif value < current.value:
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Buscando {value}: {value} < {current.value}, vai para a esquerda",
                    state={"tree": tree_to_dict(root)},
                    highlighted=[current.value],
                ))
                current = current.left
            else:
                steps.append(ExecutionStep(
                    step_number=start_step + len(steps),
                    description=f"Buscando {value}: {value} > {current.value}, vai para a direita",
                    state={"tree": tree_to_dict(root)},
                    highlighted=[current.value],
                ))
                current = current.right

        steps.append(ExecutionStep(
            step_number=start_step + len(steps),
            description=f"Buscando {value}: NÃO encontrado na árvore.",
            state={"tree": tree_to_dict(root), "found": None},
            highlighted=[],
        ))
        return steps
