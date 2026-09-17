// InputPanel: renderiza o formulário correto para cada algoritmo.
// Todos os inputs são editáveis pelo usuário.

import { useState } from "react"
import type { Algorithm } from "@/domain/Algorithm"

interface Props {
  algorithm: Algorithm
  onRun: (inputData: unknown) => void
  isLoading: boolean
}

function parseNumberList(raw: string): number[] {
  return raw.split(",").map(s => Number(s.trim())).filter(n => !isNaN(n))
}

// Input para arrays simples (ordenação)
function ArrayInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [val, setVal] = useState("5, 3, 8, 1, 9, 2, 7")
  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="arr">Array (separado por vírgulas)</label>
        <input id="arr" value={val} onChange={e => setVal(e.target.value)} placeholder="ex: 5, 3, 8, 1" />
      </div>
      <button className="run-btn" onClick={() => onRun(parseNumberList(val))} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para busca binária e dois ponteiros (array + target)
function ArrayTargetInput({ onRun, isLoading, label }: { onRun: (d: unknown) => void; isLoading: boolean; label: string }) {
  const [arr, setArr] = useState("1, 3, 5, 7, 9, 11, 13")
  const [target, setTarget] = useState("7")
  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="arr2">Array ordenado</label>
        <input id="arr2" value={arr} onChange={e => setArr(e.target.value)} />
      </div>
      <div className="input-field">
        <label htmlFor="target">{label}</label>
        <input id="target" type="number" value={target} onChange={e => setTarget(e.target.value)} style={{ width: 80 }} />
      </div>
      <button className="run-btn" onClick={() => onRun({ array: parseNumberList(arr), target: Number(target) })} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para Pilha
function StackInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [ops, setOps] = useState<{ op: string; value?: number }[]>([
    { op: "push", value: 10 }, { op: "push", value: 20 }, { op: "push", value: 30 },
    { op: "peek" }, { op: "pop" }, { op: "push", value: 5 }, { op: "pop" }, { op: "pop" },
  ])

  function addOp(op: string) {
    setOps(prev => [...prev, op === "push" ? { op, value: Math.floor(Math.random() * 50) + 1 } : { op }])
  }

  return (
    <div className="input-panel">
      <div className="ops-preview">
        {ops.map((o, i) => (
          <span key={i} className="op-badge">
            {o.op}{o.value !== undefined ? `(${o.value})` : ""}
            <button onClick={() => setOps(ops.filter((_, j) => j !== i))} className="op-remove">×</button>
          </span>
        ))}
      </div>
      <div className="ops-btns">
        <button className="op-add-btn" onClick={() => addOp("push")}>+ push</button>
        <button className="op-add-btn" onClick={() => addOp("pop")}>+ pop</button>
        <button className="op-add-btn" onClick={() => addOp("peek")}>+ peek</button>
        <button className="op-add-btn danger" onClick={() => setOps([])}>limpar</button>
      </div>
      <button className="run-btn" onClick={() => onRun(ops)} disabled={isLoading || ops.length === 0}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para Fila
function QueueInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [ops, setOps] = useState<{ op: string; value?: number }[]>([
    { op: "enqueue", value: 1 }, { op: "enqueue", value: 2 }, { op: "enqueue", value: 3 },
    { op: "peek" }, { op: "dequeue" }, { op: "enqueue", value: 4 }, { op: "dequeue" },
  ])

  function addOp(op: string) {
    setOps(prev => [...prev, op === "enqueue" ? { op, value: Math.floor(Math.random() * 50) + 1 } : { op }])
  }

  return (
    <div className="input-panel">
      <div className="ops-preview">
        {ops.map((o, i) => (
          <span key={i} className="op-badge">
            {o.op}{o.value !== undefined ? `(${o.value})` : ""}
            <button onClick={() => setOps(ops.filter((_, j) => j !== i))} className="op-remove">×</button>
          </span>
        ))}
      </div>
      <div className="ops-btns">
        <button className="op-add-btn" onClick={() => addOp("enqueue")}>+ enqueue</button>
        <button className="op-add-btn" onClick={() => addOp("dequeue")}>+ dequeue</button>
        <button className="op-add-btn" onClick={() => addOp("peek")}>+ peek</button>
        <button className="op-add-btn danger" onClick={() => setOps([])}>limpar</button>
      </div>
      <button className="run-btn" onClick={() => onRun(ops)} disabled={isLoading || ops.length === 0}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para Hash Map
function HashMapInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [val, setVal] = useState("a, b, c, a, b, a, d, c, a")
  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="hm">Elementos (separados por vírgulas)</label>
        <input id="hm" value={val} onChange={e => setVal(e.target.value)} placeholder="ex: a, b, a, c, b" />
      </div>
      <button className="run-btn" onClick={() => onRun(val.split(",").map(s => s.trim()).filter(Boolean))} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para árvores (valores para construir)
function TreeInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  // Árvore fixa editável como JSON
  const defaultTree = { value: 1, left: { value: 2, left: { value: 4, left: null, right: null }, right: { value: 5, left: null, right: null } }, right: { value: 3, left: null, right: { value: 6, left: null, right: null } } }
  return (
    <div className="input-panel">
      <p className="demo-note">Árvore binária de exemplo (valores: 1, 2, 3, 4, 5, 6)</p>
      <button className="run-btn" onClick={() => onRun(defaultTree)} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para DFS em árvore com escolha de ordem
function DFSTreeInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [order, setOrder] = useState("pre")
  const defaultTree = { value: 1, left: { value: 2, left: { value: 4, left: null, right: null }, right: { value: 5, left: null, right: null } }, right: { value: 3, left: null, right: { value: 6, left: null, right: null } } }
  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="order">Ordem de percurso</label>
        <select id="order" value={order} onChange={e => setOrder(e.target.value)} className="select-input">
          <option value="pre">Pré-ordem (raiz → esq → dir)</option>
          <option value="in">In-ordem (esq → raiz → dir)</option>
          <option value="post">Pós-ordem (esq → dir → raiz)</option>
        </select>
      </div>
      <button className="run-btn" onClick={() => onRun({ tree: defaultTree, order })} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para BST
function BSTInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const [insertVals, setInsertVals] = useState("8, 3, 10, 1, 6, 14, 4, 7")
  const [searchVal, setSearchVal] = useState("6")
  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="bst-insert">Valores para inserir (em ordem)</label>
        <input id="bst-insert" value={insertVals} onChange={e => setInsertVals(e.target.value)} />
      </div>
      <div className="input-field">
        <label htmlFor="bst-search">Valor para buscar</label>
        <input id="bst-search" type="number" value={searchVal} onChange={e => setSearchVal(e.target.value)} style={{ width: 80 }} />
      </div>
      <button className="run-btn" onClick={() => {
        const ops = parseNumberList(insertVals).map(v => ({ op: "insert", value: v }))
        ops.push({ op: "search", value: Number(searchVal) })
        onRun({ operations: ops })
      }} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Input para Grafo DFS com editor de arestas
function GraphInput({ onRun, isLoading }: { onRun: (d: unknown) => void; isLoading: boolean }) {
  const defaultGraph = { A: ["B", "C"], B: ["D", "E"], C: ["F"], D: [], E: [], F: [] }
  const [nodes, setNodes] = useState(Object.keys(defaultGraph).join(", "))
  const [edges, setEdges] = useState("A-B, A-C, B-D, B-E, C-F")
  const [start, setStart] = useState("A")

  function buildGraph() {
    const graph: Record<string, string[]> = {}
    nodes.split(",").map(n => n.trim()).filter(Boolean).forEach(n => { graph[n] = [] })
    edges.split(",").map(e => e.trim()).filter(Boolean).forEach(e => {
      const [from, to] = e.split("-").map(s => s.trim())
      if (from && to && graph[from] !== undefined) graph[from].push(to)
    })
    return graph
  }

  return (
    <div className="input-panel">
      <div className="input-field">
        <label htmlFor="gnodes">Nós (separados por vírgula)</label>
        <input id="gnodes" value={nodes} onChange={e => setNodes(e.target.value)} placeholder="ex: A, B, C" />
      </div>
      <div className="input-field">
        <label htmlFor="gedges">Arestas (ex: A-B, A-C)</label>
        <input id="gedges" value={edges} onChange={e => setEdges(e.target.value)} placeholder="ex: A-B, B-C" />
      </div>
      <div className="input-field">
        <label htmlFor="gstart">Nó inicial</label>
        <input id="gstart" value={start} onChange={e => setStart(e.target.value)} style={{ width: 60 }} />
      </div>
      <button className="run-btn" onClick={() => onRun({ graph: buildGraph(), start })} disabled={isLoading}>
        {isLoading ? "Executando..." : "Executar"}
      </button>
    </div>
  )
}

// Roteador principal
export function InputPanel({ algorithm, onRun, isLoading }: Props) {
  const id = algorithm.id

  if (["bubble_sort", "merge_sort", "quick_sort", "heap_sort"].includes(id))
    return <ArrayInput onRun={onRun} isLoading={isLoading} />

  if (id === "binary_search")
    return <ArrayTargetInput onRun={onRun} isLoading={isLoading} label="Valor a buscar" />

  if (id === "two_pointers")
    return <ArrayTargetInput onRun={onRun} isLoading={isLoading} label="Soma alvo" />

  if (id === "stack") return <StackInput onRun={onRun} isLoading={isLoading} />
  if (id === "queue") return <QueueInput onRun={onRun} isLoading={isLoading} />
  if (id === "hash_map_frequency") return <HashMapInput onRun={onRun} isLoading={isLoading} />
  if (id === "bfs_tree") return <TreeInput onRun={onRun} isLoading={isLoading} />
  if (id === "dfs_tree") return <DFSTreeInput onRun={onRun} isLoading={isLoading} />
  if (id === "bst") return <BSTInput onRun={onRun} isLoading={isLoading} />
  if (id === "dfs_graph") return <GraphInput onRun={onRun} isLoading={isLoading} />

  return null
}
