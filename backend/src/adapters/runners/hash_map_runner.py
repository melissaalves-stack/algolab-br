# Hash Map de frequência: conta quantas vezes cada elemento aparece.
# A cada elemento lido, registra um passo mostrando o estado atual do mapa.
# Input: lista de inteiros ou strings.

from src.domain.ports.algorithm_runner import AlgorithmRunner
from src.domain.entities.execution_step import ExecutionStep


class HashMapFrequencyRunner(AlgorithmRunner):

    def run(self, input_data: list) -> list[ExecutionStep]:
        steps: list[ExecutionStep] = []
        step_num = 0
        freq_map: dict = {}

        for i, item in enumerate(input_data):
            # Incrementa a contagem ou começa em 1 se for a primeira vez
            freq_map[item] = freq_map.get(item, 0) + 1

            steps.append(ExecutionStep(
                step_number=step_num,
                description=f"Lendo '{item}' no índice {i}. Contagem agora: {freq_map[item]}",
                state={"input": input_data, "map": dict(freq_map), "current_index": i},
                highlighted=[i],
            ))
            step_num += 1

        steps.append(ExecutionStep(
            step_number=step_num,
            description="Mapa de frequência completo!",
            state={"input": input_data, "map": dict(freq_map)},
            highlighted=[],
            is_final=True,
        ))
        return steps
