# Testa a API de ponta a ponta usando TestClient do FastAPI.
# Não precisa subir um servidor real — o FastAPI simula internamente.

from fastapi.testclient import TestClient
from src.infrastructure.api.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_lista_algoritmos():
    response = client.get("/algorithms/")
    assert response.status_code == 200
    algorithms = response.json()
    assert len(algorithms) > 0
    # Verifica que os campos esperados existem no primeiro item
    assert "id" in algorithms[0]
    assert "name" in algorithms[0]
    assert "time_complexity" in algorithms[0]


def test_executa_bubble_sort():
    response = client.post("/execute/", json={
        "algorithm_id": "bubble_sort",
        "input_data": [4, 2, 7, 1],
    })
    assert response.status_code == 200
    body = response.json()
    assert body["algorithm_id"] == "bubble_sort"
    assert body["total_steps"] > 0
    # O último passo deve ter o array ordenado
    last_step = body["steps"][-1]
    assert last_step["is_final"] is True
    assert last_step["state"]["array"] == [1, 2, 4, 7]


def test_algoritmo_inexistente_retorna_404():
    response = client.post("/execute/", json={
        "algorithm_id": "algoritmo_que_nao_existe",
        "input_data": [],
    })
    assert response.status_code == 404


def test_executa_binary_search():
    response = client.post("/execute/", json={
        "algorithm_id": "binary_search",
        "input_data": {"array": [1, 3, 5, 7], "target": 5},
    })
    assert response.status_code == 200
    body = response.json()
    last_step = body["steps"][-1]
    assert last_step["state"]["found_index"] == 2  # índice do 5
