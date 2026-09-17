# Vercel Serverless Function — substitui o endpoint POST /execute do FastAPI.
# Todos os runners estão aqui dentro para evitar imports entre arquivos,
# já que o Vercel executa cada arquivo de função de forma isolada.

import json
from collections import deque
from http.server import BaseHTTPRequestHandler


# ─── Runners ──────────────────────────────────────────────────────────────────

def run_bubble_sort(arr: list) -> list:
    arr = arr.copy()
    steps = []
    n = len(arr)
    step_num = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                "step_number": step_num,
                "description": f"Comparando arr[{j}]={arr[j]} com arr[{j+1}]={arr[j+1]}",
                "state": {"array": arr.copy()},
                "highlighted": [j, j + 1],
                "is_final": False,
            })
            step_num += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                    "step_number": step_num,
                    "description": f"Trocando — novo estado: {arr}",
                    "state": {"array": arr.copy()},
                    "highlighted": [j, j + 1],
                    "is_final": False,
                })
                step_num += 1

    steps.append({
        "step_number": step_num,
        "description": "Array ordenado!",
        "state": {"array": arr.copy()},
        "highlighted": [],
        "is_final": True,
    })
    return steps


def run_binary_search(data: dict) -> list:
    arr = data["array"]
    target = data["target"]
    steps = []
    step_num = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        steps.append({
            "step_number": step_num,
            "description": f"Meio no índice {mid} (valor {arr[mid]}). left={left}, right={right}",
            "state": {"array": arr, "left": left, "right": right, "mid": mid},
            "highlighted": [mid],
            "is_final": False,
        })
        step_num += 1
        if arr[mid] == target:
            steps.append({
                "step_number": step_num,
                "description": f"Encontrado! {target} está no índice {mid}.",
                "state": {"array": arr, "found_index": mid},
                "highlighted": [mid],
                "is_final": True,
            })
            return steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    steps.append({
        "step_number": step_num,
        "description": f"{target} não está no array.",
        "state": {"array": arr, "found_index": -1},
        "highlighted": [],
        "is_final": True,
    })
    return steps


def run_two_pointers(data: dict) -> list:
    arr = data["array"]
    target = data["target"]
    steps = []
    step_num = 0
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        steps.append({
            "step_number": step_num,
            "description": f"arr[{left}]={arr[left]} + arr[{right}]={arr[right]} = {current_sum}",
            "state": {"array": arr, "left": left, "right": right, "sum": current_sum},
            "highlighted": [left, right],
            "is_final": False,
        })
        step_num += 1
        if current_sum == target:
            steps.append({
                "step_number": step_num,
                "description": f"Par encontrado nos índices {left} e {right}!",
                "state": {"array": arr, "result": [left, right]},
                "highlighted": [left, right],
                "is_final": True,
            })
            return steps
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    steps.append({
        "step_number": step_num,
        "description": "Nenhum par encontrado.",
        "state": {"array": arr, "result": []},
        "highlighted": [],
        "is_final": True,
    })
    return steps


def run_hash_map(input_data: list) -> list:
    steps = []
    step_num = 0
    freq_map = {}

    for i, item in enumerate(input_data):
        freq_map[item] = freq_map.get(item, 0) + 1
        steps.append({
            "step_number": step_num,
            "description": f"Lendo '{item}' no índice {i}. Contagem: {freq_map[item]}",
            "state": {"input": input_data, "map": dict(freq_map), "current_index": i},
            "highlighted": [i],
            "is_final": False,
        })
        step_num += 1

    steps.append({
        "step_number": step_num,
        "description": "Mapa de frequência completo!",
        "state": {"input": input_data, "map": dict(freq_map)},
        "highlighted": [],
        "is_final": True,
    })
    return steps


def run_bfs_tree(node: dict) -> list:
    steps = []
    step_num = 0
    visited_order = []
    queue = deque([(node, "root")])

    while queue:
        current, node_id = queue.popleft()
        visited_order.append(current["value"])
        steps.append({
            "step_number": step_num,
            "description": f"Visitando nó {current['value']}. Ordem: {visited_order}",
            "state": {"tree": node, "visited": list(visited_order), "current": current["value"]},
            "highlighted": [current["value"]],
            "is_final": False,
        })
        step_num += 1
        if current.get("left"):
            queue.append((current["left"], f"{node_id}-left"))
        if current.get("right"):
            queue.append((current["right"], f"{node_id}-right"))

    steps.append({
        "step_number": step_num,
        "description": f"BFS completo! Ordem: {visited_order}",
        "state": {"tree": node, "visited": visited_order},
        "highlighted": [],
        "is_final": True,
    })
    return steps


def run_dfs_graph(data: dict) -> list:
    graph = data["graph"]
    start = data["start"]
    steps = []
    step_num = 0
    visited = set()
    stack = [start]
    visit_order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        visit_order.append(node)
        steps.append({
            "step_number": step_num,
            "description": f"Visitando '{node}'. Pilha: {stack}. Ordem: {visit_order}",
            "state": {
                "graph": graph,
                "visited": list(visited),
                "stack": list(stack),
                "visit_order": list(visit_order),
                "current": node,
            },
            "highlighted": [node],
            "is_final": False,
        })
        step_num += 1
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    steps.append({
        "step_number": step_num,
        "description": f"DFS completo! Ordem: {visit_order}",
        "state": {"graph": graph, "visit_order": visit_order},
        "highlighted": [],
        "is_final": True,
    })
    return steps


# ─── Roteador ─────────────────────────────────────────────────────────────────

RUNNERS = {
    "bubble_sort": run_bubble_sort,
    "binary_search": run_binary_search,
    "two_pointers": run_two_pointers,
    "hash_map_frequency": run_hash_map,
    "bfs_tree": run_bfs_tree,
    "dfs_graph": run_dfs_graph,
}


# ─── Handler HTTP ─────────────────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):

    def _send_json(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))

        algorithm_id = body.get("algorithm_id", "")
        input_data = body.get("input_data")

        runner = RUNNERS.get(algorithm_id)
        if runner is None:
            self._send_json(404, {"detail": f"Algoritmo '{algorithm_id}' não encontrado."})
            return

        try:
            steps = runner(input_data)
        except Exception as e:
            self._send_json(422, {"detail": str(e)})
            return

        self._send_json(200, {
            "algorithm_id": algorithm_id,
            "total_steps": len(steps),
            "steps": steps,
        })

    def do_OPTIONS(self):
        # Preflight CORS
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
