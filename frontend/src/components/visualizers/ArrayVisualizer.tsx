// Visualiza um array como barras verticais.
// Elementos destacados (highlighted) aparecem com cor diferente.
// A altura de cada barra é proporcional ao valor do elemento.

interface Props {
  array: number[]
  highlighted: number[]
  description: string
}

export function ArrayVisualizer({ array, highlighted, description }: Props) {
  const max = Math.max(...array, 1) // evita divisão por zero

  return (
    <div className="visualizer array-visualizer">
      <p className="step-description">{description}</p>
      <div className="bars-container" aria-label="Visualização do array">
        {array.map((value, index) => (
          <div
            key={index}
            className={`bar ${highlighted.includes(index) ? "bar--highlighted" : ""}`}
            style={{ height: `${(value / max) * 100}%` }}
            aria-label={`Índice ${index}: ${value}`}
          >
            <span className="bar-value">{value}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
