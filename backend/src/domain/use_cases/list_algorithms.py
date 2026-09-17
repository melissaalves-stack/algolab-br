# Devolve a lista de todos os algoritmos disponíveis no sistema.
# O frontend usa isso para montar o seletor de algoritmos.

from src.domain.entities.algorithm import Algorithm


# Catálogo fixo por enquanto — futuramente poderia vir de um banco de dados
AVAILABLE_ALGORITHMS: list[Algorithm] = [
    Algorithm(
        id="bubble_sort",
        name="Bubble Sort",
        category="array",
        description="Compara pares de elementos adjacentes e os troca se estiverem fora de ordem.",
        time_complexity="O(n²)",
        space_complexity="O(1)",
    ),
    Algorithm(
        id="binary_search",
        name="Binary Search",
        category="array",
        description="Divide o array ao meio repetidamente para encontrar um elemento em tempo logarítmico.",
        time_complexity="O(log n)",
        space_complexity="O(1)",
    ),
    Algorithm(
        id="two_pointers",
        name="Two Pointers",
        category="array",
        description="Usa dois índices se movendo em direções opostas para resolver problemas de par/soma.",
        time_complexity="O(n)",
        space_complexity="O(1)",
    ),
    Algorithm(
        id="hash_map_frequency",
        name="Hash Map — Frequência",
        category="hash_map",
        description="Conta a frequência de cada elemento usando um dicionário.",
        time_complexity="O(n)",
        space_complexity="O(n)",
    ),
    Algorithm(
        id="bfs_tree",
        name="BFS — Árvore",
        category="tree",
        description="Percorre uma árvore nível por nível usando uma fila.",
        time_complexity="O(n)",
        space_complexity="O(n)",
    ),
    Algorithm(
        id="dfs_graph",
        name="DFS — Grafo",
        category="graph",
        description="Percorre um grafo em profundidade usando recursão ou pilha.",
        time_complexity="O(V + E)",
        space_complexity="O(V)",
    ),
]


class ListAlgorithms:

    def execute(self) -> list[Algorithm]:
        return AVAILABLE_ALGORITHMS
