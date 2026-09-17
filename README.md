<div align="center">

# algolab

**Step through algorithms. Watch them think.**

[🇧🇷 Português](#português) · [🇺🇸 English](#english)

[![Demo](https://img.shields.io/badge/demo-live-6c8cff?style=flat-square)](https://algolab-br-j3vd-n1ryq8k5e-melissaalves-stacks-projects.vercel.app)
[![License](https://img.shields.io/badge/license-MIT-4ade80?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square)](https://python.org)
[![TypeScript](https://img.shields.io/badge/typescript-5-3178c6?style=flat-square)](https://typescriptlang.org)

**[→ abrir o app](https://algolab-br-j3vd-n1ryq8k5e-melissaalves-stacks-projects.vercel.app)**

</div>

---

## English

algolab is an interactive algorithm visualizer for CS students. Pick an algorithm, give it an input, and watch each step play out — pausing, rewinding, and stepping through at your own pace.

### Algorithms

| Category | Algorithm | Time | Space |
|---|---|---|---|
| Sorting | Bubble Sort | O(n²) | O(1) |
| Sorting | Merge Sort | O(n log n) | O(n) |
| Sorting | Quick Sort | O(n log n) | O(log n) |
| Sorting | Heap Sort | O(n log n) | O(1) |
| Search | Binary Search | O(log n) | O(1) |
| Search | Two Pointers | O(n) | O(1) |
| Linear | Stack | O(1) per op | O(n) |
| Linear | Queue | O(1) per op | O(n) |
| Hash | Frequency Count | O(n) | O(n) |
| Tree | BFS | O(n) | O(n) |
| Tree | DFS (pre/in/post) | O(n) | O(h) |
| Tree | BST Insert & Search | O(log n) avg | O(n) |
| Graph | DFS | O(V+E) | O(V) |

### Architecture

The project follows **Clean Architecture / Ports & Adapters**:

```
algolab/
├── api/                  # Vercel Serverless Functions (Python)
├── frontend/             # React + TypeScript + Vite
│   └── src/
│       ├── domain/       # Types — no framework dependencies
│       ├── application/  # Hooks (business logic, decoupled from UI)
│       ├── adapters/     # HTTP calls — only layer that touches the network
│       └── components/   # Visualizers, controls, selector
└── backend/              # Local dev server (FastAPI) — same logic, different transport
```

> Each algorithm runner is a class that implements a single interface: `run(input) → List[Step]`. The UI and the API know nothing about each other's internals.

### Running locally

**Option 1 — Docker (recommended)**
```bash
docker compose up
# Frontend: http://localhost:5173
# API docs: http://localhost:8000/docs
```

**Option 2 — Manual**
```bash
# Backend
cd backend
pip install -r requirements.txt -r requirements-dev.txt
uvicorn src.infrastructure.api.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
VITE_API_URL=http://localhost:8000 npm run dev
```

### Tests
```bash
cd backend && pytest tests/ -v
```

---

## Português

algolab é um visualizador interativo de algoritmos para estudantes de Ciência da Computação. Escolha um algoritmo, forneça um input, e assista cada passo se desenrolar — pausando, voltando e avançando no seu ritmo.

**[→ abrir o app](https://algolab-br-j3vd-n1ryq8k5e-melissaalves-stacks-projects.vercel.app)**

### Algoritmos

| Categoria | Algoritmo | Tempo | Espaço |
|---|---|---|---|
| Ordenação | Bubble Sort | O(n²) | O(1) |
| Ordenação | Merge Sort | O(n log n) | O(n) |
| Ordenação | Quick Sort | O(n log n) | O(log n) |
| Ordenação | Heap Sort | O(n log n) | O(1) |
| Busca | Binary Search | O(log n) | O(1) |
| Busca | Two Pointers | O(n) | O(1) |
| Linear | Pilha (Stack) | O(1) por op | O(n) |
| Linear | Fila (Queue) | O(1) por op | O(n) |
| Hash | Frequência | O(n) | O(n) |
| Árvore | BFS | O(n) | O(n) |
| Árvore | DFS (pré/in/pós) | O(n) | O(h) |
| Árvore | BST — Inserção e Busca | O(log n) médio | O(n) |
| Grafo | DFS | O(V+E) | O(V) |

### Arquitetura

O projeto segue **Clean Architecture / Ports & Adapters**:

```
algolab/
├── api/                  # Vercel Serverless Functions (Python)
├── frontend/             # React + TypeScript + Vite
│   └── src/
│       ├── domain/       # Tipos — sem dependência de framework
│       ├── application/  # Hooks (lógica de negócio, desacoplada da UI)
│       ├── adapters/     # Chamadas HTTP — única camada que toca a rede
│       └── components/   # Visualizadores, controles, seletor
└── backend/              # Servidor local de dev (FastAPI) — mesma lógica, transporte diferente
```

> Cada runner de algoritmo é uma classe que implementa uma única interface: `run(input) → List[Step]`. A UI e a API não sabem nada sobre os internos um do outro.

### Rodando localmente

**Opção 1 — Docker (recomendado)**
```bash
docker compose up
# Frontend: http://localhost:5173
# Docs da API: http://localhost:8000/docs
```

**Opção 2 — Manual**
```bash
# Backend
cd backend
pip install -r requirements.txt -r requirements-dev.txt
uvicorn src.infrastructure.api.main:app --reload

# Frontend (outro terminal)
cd frontend
npm install
VITE_API_URL=http://localhost:8000 npm run dev
```

### Testes
```bash
cd backend && pytest tests/ -v
```

---

<div align="center">
  <sub>Melissa Alves</sub>
</div>
