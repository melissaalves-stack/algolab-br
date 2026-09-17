# O container é o único lugar que sabe qual implementação concreta usar para cada algoritmo.

from src.adapters.runners.array_runner import BubbleSortRunner
from src.adapters.runners.merge_sort_runner import MergeSortRunner
from src.adapters.runners.quick_sort_runner import QuickSortRunner
from src.adapters.runners.heap_sort_runner import HeapSortRunner
from src.adapters.runners.binary_search_runner import BinarySearchRunner
from src.adapters.runners.two_pointers_runner import TwoPointersRunner
from src.adapters.runners.stack_runner import StackRunner
from src.adapters.runners.queue_runner import QueueRunner
from src.adapters.runners.hash_map_runner import HashMapFrequencyRunner
from src.adapters.runners.tree_traversal_runner import BFSTreeRunner
from src.adapters.runners.dfs_tree_runner import DFSTreeRunner
from src.adapters.runners.bst_runner import BSTRunner
from src.adapters.runners.graph_traversal_runner import DFSGraphRunner
from src.domain.ports.algorithm_runner import AlgorithmRunner

_RUNNERS: dict[str, AlgorithmRunner] = {
    "bubble_sort": BubbleSortRunner(),
    "merge_sort": MergeSortRunner(),
    "quick_sort": QuickSortRunner(),
    "heap_sort": HeapSortRunner(),
    "binary_search": BinarySearchRunner(),
    "two_pointers": TwoPointersRunner(),
    "stack": StackRunner(),
    "queue": QueueRunner(),
    "hash_map_frequency": HashMapFrequencyRunner(),
    "bfs_tree": BFSTreeRunner(),
    "dfs_tree": DFSTreeRunner(),
    "bst": BSTRunner(),
    "dfs_graph": DFSGraphRunner(),
}


def get_runner(algorithm_id: str) -> AlgorithmRunner:
    runner = _RUNNERS.get(algorithm_id)
    if runner is None:
        raise KeyError(f"Algoritmo '{algorithm_id}' não encontrado.")
    return runner
