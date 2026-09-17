# Rota POST /execute — recebe algoritmo + input, devolve todos os passos.
# Em caso de algoritmo inexistente ou input inválido, devolve erro HTTP adequado.

from fastapi import APIRouter, HTTPException
from src.domain.use_cases.run_algorithm import RunAlgorithm
from src.infrastructure.container import get_runner
from src.infrastructure.api.schemas.request import AlgorithmRunRequest
from src.infrastructure.api.schemas.response import ExecutionResponse, StepResponse

router = APIRouter(prefix="/execute", tags=["executions"])


@router.post("/", response_model=ExecutionResponse)
def execute_algorithm(request: AlgorithmRunRequest):
    try:
        runner = get_runner(request.algorithm_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    try:
        use_case = RunAlgorithm(runner)
        steps = use_case.execute(request.input_data)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # Monta a resposta convertendo cada ExecutionStep em StepResponse
    return ExecutionResponse(
        algorithm_id=request.algorithm_id,
        total_steps=len(steps),
        steps=[StepResponse(**vars(step)) for step in steps],
    )
