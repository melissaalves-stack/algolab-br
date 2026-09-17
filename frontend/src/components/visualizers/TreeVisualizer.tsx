// Renderiza uma árvore binária como SVG.
// Nós visitados ficam destacados; o nó atual tem cor diferente.
// Usa layout recursivo simples: nó raiz no topo, filhos abaixo.

export interface TreeNode {
  value: number
  left?: TreeNode | null
  right?: TreeNode | null
}

interface Props {
  tree: TreeNode
  visited: number[]
  current: number | null
  description: string
}

interface NodeLayout {
  value: number
  x: number
  y: number
  parentX?: number
  parentY?: number
}

// Calcula as posições (x, y) de cada nó recursivamente
function layoutTree(
  node: TreeNode | null | undefined,
  x: number,
  y: number,
  spread: number,
  result: NodeLayout[],
  parentX?: number,
  parentY?: number,
) {
  if (!node) return
  result.push({ value: node.value, x, y, parentX, parentY })
  layoutTree(node.left, x - spread, y + 70, spread / 2, result, x, y)
  layoutTree(node.right, x + spread, y + 70, spread / 2, result, x, y)
}

export function TreeVisualizer({ tree, visited, current, description }: Props) {
  const nodes: NodeLayout[] = []
  layoutTree(tree, 300, 50, 120, nodes)

  return (
    <div className="visualizer tree-visualizer">
      <p className="step-description">{description}</p>
      <svg width="600" height="300" aria-label="Visualização da árvore">
        {nodes.map((node, i) =>
          node.parentX !== undefined ? (
            // Aresta entre nó e seu pai
            <line
              key={`edge-${i}`}
              x1={node.parentX}
              y1={node.parentY}
              x2={node.x}
              y2={node.y}
              className="tree-edge"
            />
          ) : null,
        )}
        {nodes.map((node, i) => {
          const isVisited = visited.includes(node.value)
          const isCurrent = node.value === current
          return (
            <g key={`node-${i}`} aria-label={`Nó ${node.value}`}>
              <circle
                cx={node.x}
                cy={node.y}
                r={22}
                className={`tree-node ${isCurrent ? "tree-node--current" : isVisited ? "tree-node--visited" : ""}`}
              />
              <text x={node.x} y={node.y + 5} textAnchor="middle" className="tree-label">
                {node.value}
              </text>
            </g>
          )
        })}
      </svg>
    </div>
  )
}
