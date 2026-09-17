// Visualiza Pilha e Fila como caixas empilhadas/enfileiradas.

interface Props {
  items: unknown[]
  highlighted: number[]
  description: string
  type: "stack" | "queue"
  removed?: unknown
}

export function StackQueueVisualizer({ items, highlighted, description, type, removed }: Props) {
  const displayItems = type === "stack" ? [...items].reverse() : items

  return (
    <div className="visualizer sq-visualizer">
      <p className="step-description">{description}</p>

      {removed !== undefined && (
        <div className="sq-removed">← removido: <strong>{String(removed)}</strong></div>
      )}

      <div className={`sq-container sq-${type}`}>
        {displayItems.length === 0 ? (
          <div className="sq-empty">vazio</div>
        ) : (
          displayItems.map((item, i) => {
            const realIndex = type === "stack" ? items.length - 1 - i : i
            const isHighlighted = highlighted.includes(realIndex)
            const isFirst = i === 0
            return (
              <div key={i} className={`sq-item ${isHighlighted ? "sq-item--active" : ""}`}>
                <span className="sq-value">{String(item)}</span>
                {isFirst && (
                  <span className="sq-label">{type === "stack" ? "topo" : "frente"}</span>
                )}
              </div>
            )
          })
        )}
      </div>

      <div className="sq-info">
        <span>Tipo: <strong>{type === "stack" ? "LIFO" : "FIFO"}</strong></span>
        <span>Tamanho: <strong>{items.length}</strong></span>
      </div>
    </div>
  )
}
