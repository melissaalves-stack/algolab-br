// Renderiza um grafo como SVG com posições fixas para os nós.
// Nós visitados e o nó atual ficam com cores diferentes.
// O grafo de demo tem nós A–F dispostos em layout de árvore.

interface Props {
  graph: Record<string, string[]>
  visited: string[]
  current: string | null
  stack: string[]
  description: string
}

// Posições fixas para o grafo de demo (A–F)
const NODE_POSITIONS: Record<string, { x: number; y: number }> = {
  A: { x: 300, y: 40 },
  B: { x: 160, y: 130 },
  C: { x: 440, y: 130 },
  D: { x: 80,  y: 230 },
  E: { x: 240, y: 230 },
  F: { x: 440, y: 230 },
}

export function GraphVisualizer({ graph, visited, current, stack, description }: Props) {
  return (
    <div className="visualizer graph-visualizer">
      <p className="step-description">{description}</p>
      <svg width="560" height="290" aria-label="Visualização do grafo">
        {Object.entries(graph).map(([from, neighbors]) =>
          neighbors.map(to => {
            const p1 = NODE_POSITIONS[from]
            const p2 = NODE_POSITIONS[to]
            if (!p1 || !p2) return null
            return (
              <line
                key={`${from}-${to}`}
                x1={p1.x} y1={p1.y}
                x2={p2.x} y2={p2.y}
                className="graph-edge"
              />
            )
          }),
        )}

        {Object.keys(NODE_POSITIONS).map(nodeId => {
          const pos = NODE_POSITIONS[nodeId]
          const isCurrent = nodeId === current
          const isVisited = visited.includes(nodeId)
          const isInStack = stack.includes(nodeId)
          return (
            <g key={nodeId} aria-label={`Nó ${nodeId}`}>
              <circle
                cx={pos.x} cy={pos.y} r={24}
                className={`graph-node ${isCurrent ? "graph-node--current" : isVisited ? "graph-node--visited" : isInStack ? "graph-node--in-stack" : ""}`}
              />
              <text x={pos.x} y={pos.y + 5} textAnchor="middle" className="graph-label">
                {nodeId}
              </text>
            </g>
          )
        })}
      </svg>

      <div className="graph-legend">
        <span className="legend-item legend-item--current">atual</span>
        <span className="legend-item legend-item--visited">visitado</span>
        <span className="legend-item legend-item--stack">na pilha</span>
      </div>
    </div>
  )
}
