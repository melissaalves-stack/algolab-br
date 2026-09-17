# Catálogo completo de algoritmos disponíveis no AlgoLab.
# Baseado no programa da disciplina AEDs II — UNIFAL-MG.

from src.domain.entities.algorithm import Algorithm

AVAILABLE_ALGORITHMS: list[Algorithm] = [
    # Arrays — ordenação
    Algorithm(id="bubble_sort", name="Bubble Sort", category="ordenação",
        description="Compara pares adjacentes e os troca se estiverem fora de ordem. Simples, mas lento para arrays grandes.",
        time_complexity="O(n²)", space_complexity="O(1)"),
    Algorithm(id="merge_sort", name="Merge Sort", category="ordenação",
        description="Divide o array ao meio recursivamente e mescla as metades ordenadas. Garante O(n log n) sempre.",
        time_complexity="O(n log n)", space_complexity="O(n)"),
    Algorithm(id="quick_sort", name="Quick Sort", category="ordenação",
        description="Escolhe um pivô e particiona o array. Na média é o mais rápido na prática.",
        time_complexity="O(n log n)", space_complexity="O(log n)"),
    Algorithm(id="heap_sort", name="Heap Sort", category="ordenação",
        description="Constrói um max-heap e extrai o maior elemento repetidamente. Garante O(n log n) sem espaço extra.",
        time_complexity="O(n log n)", space_complexity="O(1)"),

    # Arrays — busca
    Algorithm(id="binary_search", name="Binary Search", category="busca",
        description="Divide o array ordenado ao meio repetidamente. Muito mais rápido que busca linear.",
        time_complexity="O(log n)", space_complexity="O(1)"),
    Algorithm(id="two_pointers", name="Two Pointers", category="busca",
        description="Dois índices se movendo em direções opostas. Resolve problemas de par/soma em tempo linear.",
        time_complexity="O(n)", space_complexity="O(1)"),

    # Estruturas lineares
    Algorithm(id="stack", name="Pilha (Stack)", category="estrutura linear",
        description="LIFO: último a entrar, primeiro a sair. Simule push, pop e peek.",
        time_complexity="O(1) por operação", space_complexity="O(n)"),
    Algorithm(id="queue", name="Fila (Queue)", category="estrutura linear",
        description="FIFO: primeiro a entrar, primeiro a sair. Simule enqueue, dequeue e peek.",
        time_complexity="O(1) por operação", space_complexity="O(n)"),

    # Hash
    Algorithm(id="hash_map_frequency", name="Hash Map — Frequência", category="hash",
        description="Conta a frequência de cada elemento usando um dicionário. Base para muitos problemas de LeetCode.",
        time_complexity="O(n)", space_complexity="O(n)"),

    # Árvores
    Algorithm(id="bfs_tree", name="BFS — Árvore", category="árvore",
        description="Percorre nível por nível usando uma fila. Útil para encontrar o caminho mais curto.",
        time_complexity="O(n)", space_complexity="O(n)"),
    Algorithm(id="dfs_tree", name="DFS — Árvore", category="árvore",
        description="Percorre em profundidade. Escolha entre pré-ordem, in-ordem e pós-ordem.",
        time_complexity="O(n)", space_complexity="O(h)"),
    Algorithm(id="bst", name="BST — Inserção e Busca", category="árvore",
        description="Árvore Binária de Busca: insira valores e veja como a árvore cresce. Busca em O(log n) se balanceada.",
        time_complexity="O(log n) médio", space_complexity="O(n)"),

    # Grafos
    Algorithm(id="dfs_graph", name="DFS — Grafo", category="grafo",
        description="Percorre em profundidade usando uma pilha. Útil para detectar ciclos e componentes conectados.",
        time_complexity="O(V + E)", space_complexity="O(V)"),
]


class ListAlgorithms:
    def execute(self) -> list[Algorithm]:
        return AVAILABLE_ALGORITHMS
