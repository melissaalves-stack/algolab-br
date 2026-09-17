// Lista os algoritmos disponíveis e permite selecionar um.
// Agrupa por categoria para facilitar a navegação.

import type { Algorithm } from "@/domain/Algorithm"

interface Props {
  algorithms: Algorithm[]
  selectedId: string | null
  onSelect: (algorithm: Algorithm) => void
}

// Agrupa um array de algoritmos por categoria
function groupByCategory(algorithms: Algorithm[]): Record<string, Algorithm[]> {
  return algorithms.reduce((groups, algo) => {
    const key = algo.category
    return { ...groups, [key]: [...(groups[key] ?? []), algo] }
  }, {} as Record<string, Algorithm[]>)
}

export function AlgorithmSelector({ algorithms, selectedId, onSelect }: Props) {
  const groups = groupByCategory(algorithms)

  return (
    <nav aria-label="Algoritmos disponíveis">
      {Object.entries(groups).map(([category, algos]) => (
        <div key={category} className="category-group">
          <span className="category-label">{category}</span>
          {algos.map(algo => (
            <button
              key={algo.id}
              onClick={() => onSelect(algo)}
              className={`algo-btn ${selectedId === algo.id ? "selected" : ""}`}
              aria-pressed={selectedId === algo.id}
            >
              {algo.name}
            </button>
          ))}
        </div>
      ))}
    </nav>
  )
}
