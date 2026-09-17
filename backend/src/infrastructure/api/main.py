from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.api.routers import algorithms, executions

app = FastAPI(
    title="AlgoLab API",
    description="API que executa algoritmos passo a passo para visualização.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(algorithms.router)
app.include_router(executions.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
