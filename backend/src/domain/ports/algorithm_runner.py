# Uma "porta" é uma interface — ela define o contrato sem dizer como implementar.
# Cada runner concreto (bubble sort, DFS etc.) vai herdar dessa classe
# e implementar o método run(). O use case não sabe qual runner está usando —
# só sabe que ele tem esse método. Isso é o coração de Ports & Adapters.

from abc import ABC, abstractmethod
from typing import Any
from src.domain.entities.execution_step import ExecutionStep


class AlgorithmRunner(ABC):

    @abstractmethod
    def run(self, input_data: Any) -> list[ExecutionStep]:
        # Executa o algoritmo e devolve todos os passos da execução.
        # O input_data varia por algoritmo (lista, grafo, etc).
        ...
