from src.adapters.runners.binary_search_runner import BinarySearchRunner


def test_encontra_elemento_existente():
    runner = BinarySearchRunner()
    steps = runner.run({"array": [1, 3, 5, 7, 9], "target": 7})

    final_step = steps[-1]
    assert final_step.is_final is True
    assert final_step.state["found_index"] == 3  # índice do 7


def test_nao_encontra_elemento_inexistente():
    runner = BinarySearchRunner()
    steps = runner.run({"array": [1, 3, 5, 7, 9], "target": 4})

    final_step = steps[-1]
    assert final_step.is_final is True
    assert final_step.state["found_index"] == -1


def test_encontra_no_primeiro_elemento():
    runner = BinarySearchRunner()
    steps = runner.run({"array": [2, 4, 6], "target": 2})
    assert steps[-1].state["found_index"] == 0
