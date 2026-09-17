// Única camada que sabe o endereço da API.
// O resto do frontend nunca chama fetch diretamente — sempre usa essas funções.
// Se a URL da API mudar, só muda aqui.

import type { Algorithm, ExecutionResult } from "@/domain/Algorithm"

const BASE_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000"

export async function fetchAlgorithms(): Promise<Algorithm[]> {
  const response = await fetch(`${BASE_URL}/algorithms/`)
  if (!response.ok) throw new Error("Erro ao buscar algoritmos.")
  return response.json()
}

export async function executeAlgorithm(
  algorithmId: string,
  inputData: unknown,
): Promise<ExecutionResult> {
  const response = await fetch(`${BASE_URL}/execute/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ algorithm_id: algorithmId, input_data: inputData }),
  })
  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail ?? "Erro ao executar algoritmo.")
  }
  return response.json()
}
