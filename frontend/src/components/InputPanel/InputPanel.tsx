// Renderiza o formulário de input correto para cada algoritmo.
// Algoritmos de array pedem uma lista; busca binária e dois ponteiros pedem lista + target.

import { useState } from "react"
import type { Algorithm } from "@/domain/Algorithm"

interface Props {
  algorithm: Algorithm
  onRun: (inputData: unknown) => void
  isLoading: boolean
}

// Converte "3, 1, 4, 1, 5" → [3, 1, 4, 1, 5]
function parseNumberList(raw: string): number[] {
  return raw.split(",").map(s => Number(s.trim())).filter(n => !isNaN(n))
}

export function InputPanel({ algorithm, onRun, isLoading }: Props) {
  const [arrayInput, setArrayInput] = useState("5, 3, 8, 1, 9, 2")
  const [targetInput, setTargetInput] = useState("8")

  const needsTarget = ["binary_search", "two_pointers"].includes(algorithm.id)
  const isGraph = algorithm.id === "dfs_graph"
  const isTree = algorithm.id === "bfs_tree"

  function handleSubmit() {
    if (isGraph) {
      // Grafo fixo para demo — o usuário pode expandir isso depois
      onRun({
        graph: { A: ["B", "C"], B: ["D", "E"], C: ["F"], D: [], E: [], F: [] },
        start: "A",
      })
      return
    }

    if (isTree) {
      // Árvore binária fixa para demo
      onRun({
        value: 1,
        left: { value: 2, left: { value: 4, left: null, right: null }, right: { value: 5, left: null, right: null } },
        right: { value: 3, left: null, right: { value: 6, left: null, right: null } },
      })
      return
    }

    const array = parseNumberList(arrayInput)
    onRun(needsTarget ? { array, target: Number(targetInput) } : array)
  }

  return (
    <div className="input-panel">
      {!isGraph && !isTree && (
        <div className="input-field">
          <label htmlFor="array-input">Array (separado por vírgulas)</label>
          <input
            id="array-input"
            type="text"
            value={arrayInput}
            onChange={e => setArrayInput(e.target.value)}
            placeholder="ex: 5, 3, 8, 1"
          />
        </div>
      )}

      {needsTarget && (
        <div className="input-field">
          <label htmlFor="target-input">Alvo</label>
          <input
            id="target-input"
            type="number"
            value={targetInput}
            onChange={e => setTargetInput(e.target.value)}
          />
        </div>
      )}

      {(isGraph || isTree) && (
        <p className="demo-note">
          Usando estrutura de exemplo. Você pode editar o código para personalizar.
        </p>
      )}

      <button onClick={handleSubmit} disabled={isLoading} className="run-btn">
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}
