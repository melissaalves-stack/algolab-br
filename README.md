<div align="center">

# algolab

**Step through algorithms. Watch them think.**

[🇧🇷 Português](#português) · [🇺🇸 English](#english)

[![Demo](https://img.shields.io/badge/demo-live-6c8cff?style=flat-square)](https://your-deploy-url.vercel.app)
[![License](https://img.shields.io/badge/license-MIT-4ade80?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square)](https://python.org)
[![TypeScript](https://img.shields.io/badge/typescript-5-3178c6?style=flat-square)](https://typescriptlang.org)

</div>

---

## English

algolab is an interactive algorithm visualizer for CS students. Pick an algorithm, give it an input, and watch each step play out — pausing, rewinding, and stepping through at your own pace.

### Algorithms

| Category | Algorithm | Time | Space |
|---|---|---|---|
| Array | Bubble Sort | O(n²) | O(1) |
| Array | Binary Search | O(log n) | O(1) |
| Array | Two Pointers | O(n) | O(1) |
| Hash Map | Frequency Count | O(n) | O(n) |
| Tree | BFS | O(n) | O(n) |
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

### Deploying to Vercel

```bash
npm i -g vercel
vercel
```

The `vercel.json` at the root handles everything: it builds the frontend, routes `/api/*` to the serverless Python functions, and serves the static output from `frontend/dist`.

---

## Português

algolab é um visualizador interativo de algoritmos para estudantes de Ciência da Computação. Escolha um algoritmo, forneça um input, e assista cada passo se desenrolar — pausando, voltando e avançando no seu ritmo.

### Algoritmos

| Categoria | Algoritmo | Tempo | Espaço |
|---|---|---|---|
| Array | Bubble Sort | O(n²) | O(1) |
| Array | Binary Search | O(log n) | O(1) |
| Array | Two Pointers | O(n) | O(1) |
| Hash Map | Contagem de Frequência | O(n) | O(n) |
| Árvore | BFS | O(n) | O(n) |
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

### Deploy no Vercel

```bash
npm i -g vercel
vercel
```

O `vercel.json` na raiz cuida de tudo: faz o build do frontend, roteia `/api/*` para as serverless functions Python, e serve o output estático de `frontend/dist`.

---

<div align="center">
  <sub>Melissa Alves</sub>
</div>
