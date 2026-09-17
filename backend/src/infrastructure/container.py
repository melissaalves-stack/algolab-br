# O container é o único lugar que sabe qual implementação concreta usar.
# Quando o código quer um runner de bubble_sort, pede ao container —
# não precisa importar o BubbleSortRunner diretamente em nenhum outro lugar.
# Isso facilita muito a hora de trocar uma implementação por outra.

from src.adapters.runners.array_runner import BubbleSortRunner
from src.adapters.runners.binary_search_runner import BinarySearchRunner
from src.adapters.runners.two_pointers_runner import TwoPointersRunner
from src.adapters.runners.hash_map_runner import HashMapFrequencyRunner
from src.adapters.runners.tree_traversal_runner import BFSTreeRunner
from src.adapters.runners.graph_traversal_runner import DFSGraphRunner
from src.domain.ports.algorithm_runner import AlgorithmRunner


# Mapa de id do algoritmo → runner correspondente
_RUNNERS: dict[str, AlgorithmRunner] = {
    "bubble_sort": BubbleSortRunner(),
    "binary_search": BinarySearchRunner(),
    "two_pointers": TwoPointersRunner(),
    "hash_map_frequency": HashMapFrequencyRunner(),
    "bfs_tree": BFSTreeRunner(),
    "dfs_graph": DFSGraphRunner(),
}


def get_runner(algorithm_id: str) -> AlgorithmRunner:
    runner = _RUNNERS.get(algorithm_id)
    if runner is None:
        raise KeyError(f"Algoritmo '{algorithm_id}' não encontrado.")
    return runner
