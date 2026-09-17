# Ponto de entrada da aplicação FastAPI.
# Aqui configuramos CORS (para o frontend poder chamar a API) e registramos os routers.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.api.routers import algorithms, executions

app = FastAPI(
    title="Algo Visual API",
    description="API que executa algoritmos passo a passo para visualização.",
    version="1.0.0",
)

# CORS: permite que o frontend (rodando em outra porta) acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # porta padrão do Vite
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(algorithms.router)
app.include_router(executions.router)


@app.get("/health")
def health_check():
    # Rota simples para confirmar que a API está no ar
    return {"status": "ok"}
