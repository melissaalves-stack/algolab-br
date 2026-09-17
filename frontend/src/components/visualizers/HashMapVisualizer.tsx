// Exibe o mapa de frequência como uma tabela de chave → contagem.
// O item do array atualmente sendo lido fica destacado.

interface Props {
  input: unknown[]
  map: Record<string, number>
  currentIndex: number
  description: string
}

export function HashMapVisualizer({ input, map, currentIndex, description }: Props) {
  return (
    <div className="visualizer hash-map-visualizer">
      <p className="step-description">{description}</p>

      <div className="hm-layout">
        <div className="hm-array">
          <span className="hm-section-title">Array de entrada</span>
          {input.map((item, i) => (
            <span
              key={i}
              className={`hm-cell ${i === currentIndex ? "hm-cell--active" : ""}`}
            >
              {String(item)}
            </span>
          ))}
        </div>

        <div className="hm-map">
          <span className="hm-section-title">Hash map</span>
          {Object.entries(map).map(([key, count]) => (
            <div key={key} className="hm-entry">
              <span className="hm-key">{key}</span>
              <span className="hm-arrow">→</span>
              <span className="hm-count">{count}</span>
            </div>
          ))}
          {Object.keys(map).length === 0 && (
            <span className="hm-empty">vazio</span>
          )}
        </div>
      </div>
    </div>
  )
}
