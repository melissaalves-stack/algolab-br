# Testa o BubbleSortRunner isoladamente — sem API, sem banco, sem nada externo.
# Isso é um teste unitário puro: entra input, verifica output.

import pytest
from src.adapters.runners.array_runner import BubbleSortRunner


def test_bubble_sort_array_desordenado():
    runner = BubbleSortRunner()
    steps = runner.run([3, 1, 2])

    # O último passo deve ter o array ordenado
    final_step = steps[-1]
    assert final_step.is_final is True
    assert final_step.state["array"] == [1, 2, 3]


def test_bubble_sort_array_ja_ordenado():
    runner = BubbleSortRunner()
    steps = runner.run([1, 2, 3])

    final_step = steps[-1]
    assert final_step.state["array"] == [1, 2, 3]


def test_bubble_sort_array_unico_elemento():
    runner = BubbleSortRunner()
    steps = runner.run([42])

    # Com um elemento, vai direto pro passo final
    assert steps[-1].is_final is True
    assert steps[-1].state["array"] == [42]


def test_bubble_sort_nao_modifica_input_original():
    runner = BubbleSortRunner()
    original = [5, 3, 1]
    runner.run(original)

    # O runner nunca deve mudar a lista que recebeu
    assert original == [5, 3, 1]
