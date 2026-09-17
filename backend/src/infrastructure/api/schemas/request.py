# Schemas de entrada da API.
# O FastAPI usa esses modelos para validar automaticamente o JSON que chega.
# Se o campo obrigatório faltar, o FastAPI já devolve erro 422 sem você precisar checar.

from pydantic import BaseModel
from typing import Any


class AlgorithmRunRequest(BaseModel):
    algorithm_id: str   # ex: "bubble_sort"
    input_data: Any     # o formato varia por algoritmo (lista, dict etc.)
