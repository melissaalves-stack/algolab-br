# Vercel Serverless Function — substitui o endpoint GET /algorithms do FastAPI.
# O Vercel chama a função `handler` automaticamente quando alguém acessa /api/algorithms.
# Não precisa de servidor rodando: o Vercel instancia essa função sob demanda.

import json
from http.server import BaseHTTPRequestHandler


ALGORITHMS = [
    {
        "id": "bubble_sort",
        "name": "Bubble Sort",
        "category": "array",
        "description": "Compara pares adjacentes e os troca se estiverem fora de ordem.",
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)",
    },
    {
        "id": "binary_search",
        "name": "Binary Search",
        "category": "array",
        "description": "Divide o array ao meio repetidamente para encontrar um elemento.",
        "time_complexity": "O(log n)",
        "space_complexity": "O(1)",
    },
    {
        "id": "two_pointers",
        "name": "Two Pointers",
        "category": "array",
        "description": "Dois índices se movendo em direções opostas para resolver problemas de par/soma.",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
    },
    {
        "id": "hash_map_frequency",
        "name": "Hash Map — Frequência",
        "category": "hash_map",
        "description": "Conta a frequência de cada elemento usando um dicionário.",
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
    },
    {
        "id": "bfs_tree",
        "name": "BFS — Árvore",
        "category": "tree",
        "description": "Percorre uma árvore nível por nível usando uma fila.",
        "time_complexity": "O(n)",
        "space_complexity": "O(n)",
    },
    {
        "id": "dfs_graph",
        "name": "DFS — Grafo",
        "category": "graph",
        "description": "Percorre um grafo em profundidade usando uma pilha.",
        "time_complexity": "O(V + E)",
        "space_complexity": "O(V)",
    },
]


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(ALGORITHMS).encode())

    def do_OPTIONS(self):
        # Responde ao preflight do browser para CORS
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
