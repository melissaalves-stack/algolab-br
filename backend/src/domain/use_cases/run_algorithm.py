# O use case é o maestro: ele recebe o input do usuário,
# chama o runner certo e devolve os passos.
# Ele não sabe nada sobre HTTP, JSON ou banco de dados —
# só fala a linguagem do domínio.

from typing import Any
from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class RunAlgorithm:

    def __init__(self, runner: AlgorithmRunner):
        # O runner é injetado — poderia ser qualquer implementação
        self._runner = runner

    def execute(self, input_data: Any) -> list[ExecutionStep]:
        # Valida que o input não está vazio e dispara a execução
        if input_data is None:
            raise ValueError("Input não pode ser vazio.")
        return self._runner.run(input_data)
