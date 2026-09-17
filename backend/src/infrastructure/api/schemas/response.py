# Schemas de saída — o que a API devolve ao frontend.
# Pydantic converte os objetos de domínio nesses formatos automaticamente.

from pydantic import BaseModel
from typing import Any


class StepResponse(BaseModel):
    step_number: int
    description: str
    state: dict[str, Any]
    highlighted: list
    is_final: bool


class AlgorithmInfoResponse(BaseModel):
    id: str
    name: str
    category: str
    description: str
    time_complexity: str
    space_complexity: str


class ExecutionResponse(BaseModel):
    algorithm_id: str
    total_steps: int
    steps: list[StepResponse]
