# algo·visual

Visualizador interativo de algoritmos passo a passo.
Projeto de portfólio — Computer Science @ UNIFAL-MG.

## Algoritmos implementados

- **Arrays:** Bubble Sort, Binary Search, Two Pointers
- **Hash Map:** Frequência de elementos
- **Árvore:** BFS (Busca em Largura)
- **Grafo:** DFS (Busca em Profundidade)

## Stack

- **Backend:** Python 3.12 + FastAPI (Clean Architecture / Ports & Adapters)
- **Frontend:** React + TypeScript + Vite

## Rodando com Docker

```bash
docker compose up
```

- App: http://localhost:5173
- API: http://localhost:8000
- Docs interativos da API: http://localhost:8000/docs

## Rodando localmente (sem Docker)

**Backend:**
```bash
cd backend
pip install -r requirements.txt -r requirements-dev.txt
uvicorn src.infrastructure.api.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Testes

```bash
cd backend
pytest tests/ -v
```

## Estrutura do projeto

```
algo-visual/
├── backend/               # Python / FastAPI
│   └── src/
│       ├── domain/        # Entidades, portas, use cases (sem framework)
│       ├── adapters/      # Runners concretos de cada algoritmo
│       └── infrastructure/# API HTTP, schemas, container de dependências
└── frontend/              # React + TypeScript
    └── src/
        ├── domain/        # Tipos TypeScript
        ├── application/   # Hooks (lógica desacoplada de UI)
        ├── adapters/      # Chamadas HTTP à API
        └── components/    # Visualizadores e controles
```
