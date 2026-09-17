# Um "passo" é um snapshot do estado da estrutura de dados durante a execução.
# O frontend vai receber uma lista de passos e animar um por um.
# "highlighted" são os índices/nós que devem ficar coloridos nesse passo.

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ExecutionStep:
    step_number: int
    description: str              # o que está acontecendo nesse passo (ex: "Comparando 3 e 5")
    state: dict[str, Any]         # estado atual da estrutura (ex: {"array": [3, 5, 1]})
    highlighted: list[int] = field(default_factory=list)  # índices/nós em destaque
    is_final: bool = False        # True no último passo
