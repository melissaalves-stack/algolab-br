// Hook que busca a lista de algoritmos disponíveis ao montar o componente.
// Gerencia os três estados clássicos de uma requisição: carregando, dados, erro.

import { useEffect, useState } from "react"
import type { Algorithm } from "@/domain/Algorithm"
import { fetchAlgorithms } from "@/adapters/api/algorithmApi"

export function useAlgorithmList() {
  const [algorithms, setAlgorithms] = useState<Algorithm[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchAlgorithms()
      .then(setAlgorithms)
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false))
  }, []) // [] = roda só uma vez, quando o componente monta

  return { algorithms, loading, error }
}
