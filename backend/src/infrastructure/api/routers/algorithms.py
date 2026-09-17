# Rota GET /algorithms — devolve a lista de algoritmos disponíveis.
# O router é só a "porta de entrada" HTTP; ele delega pro use case imediatamente.

from fastapi import APIRouter
from src.domain.use_cases.list_algorithms import ListAlgorithms
from src.infrastructure.api.schemas.response import AlgorithmInfoResponse

router = APIRouter(prefix="/algorithms", tags=["algorithms"])

_list_algorithms = ListAlgorithms()


@router.get("/", response_model=list[AlgorithmInfoResponse])
def list_algorithms():
    algorithms = _list_algorithms.execute()
    # Converte cada entidade de domínio para o schema de resposta
    return [AlgorithmInfoResponse(**vars(algo)) for algo in algorithms]
