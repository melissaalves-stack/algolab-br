import { useState } from "react"
import type { Algorithm, ExecutionStep } from "@/domain/Algorithm"
import { useAlgorithmList } from "@/application/useAlgorithmList"
import { useAlgorithmRunner } from "@/application/useAlgorithmRunner"
import { AlgorithmSelector } from "@/components/AlgorithmSelector/AlgorithmSelector"
import { InputPanel } from "@/components/InputPanel/InputPanel"
import { ControlBar } from "@/components/ControlBar/ControlBar"
import { ArrayVisualizer } from "@/components/visualizers/ArrayVisualizer"
import { HashMapVisualizer } from "@/components/visualizers/HashMapVisualizer"
import { TreeVisualizer } from "@/components/visualizers/TreeVisualizer"
import { GraphVisualizer } from "@/components/visualizers/GraphVisualizer"
import { StackQueueVisualizer } from "@/components/visualizers/StackQueueVisualizer"
import type { TreeNode } from "@/components/visualizers/TreeVisualizer"

const ARRAY_IDS = ["bubble_sort", "merge_sort", "quick_sort", "heap_sort", "binary_search", "two_pointers"]
const TREE_IDS = ["bfs_tree", "dfs_tree", "bst"]

function renderVisualizer(algorithm: Algorithm, step: ExecutionStep) {
  const s = step.state as Record<string, unknown>
  const highlighted = step.highlighted as number[]

  if (ARRAY_IDS.includes(algorithm.id)) {
    return (
      <ArrayVisualizer
        array={(s.array as number[]) ?? []}
        highlighted={highlighted}
        description={step.description}
      />
    )
  }

  if (algorithm.id === "stack") {
    return (
      <StackQueueVisualizer
        items={(s.stack as unknown[]) ?? []}
        highlighted={highlighted}
        description={step.description}
        type="stack"
        removed={s.removed}
      />
    )
  }

  if (algorithm.id === "queue") {
    return (
      <StackQueueVisualizer
        items={(s.queue as unknown[]) ?? []}
        highlighted={highlighted}
        description={step.description}
        type="queue"
        removed={s.removed}
      />
    )
  }

  if (algorithm.id === "hash_map_frequency") {
    return (
      <HashMapVisualizer
        input={(s.input as unknown[]) ?? []}
        map={(s.map as Record<string, number>) ?? {}}
        currentIndex={(s.current_index as number) ?? -1}
        description={step.description}
      />
    )
  }

  if (TREE_IDS.includes(algorithm.id)) {
    return (
      <TreeVisualizer
        tree={(s.tree as TreeNode) ?? { value: 0 }}
        visited={(s.visited as number[]) ?? []}
        current={(s.current as number) ?? null}
        description={step.description}
      />
    )
  }

  if (algorithm.id === "dfs_graph") {
    return (
      <GraphVisualizer
        graph={(s.graph as Record<string, string[]>) ?? {}}
        visited={(s.visited as string[]) ?? []}
        current={(s.current as string) ?? null}
        stack={(s.stack as string[]) ?? []}
        description={step.description}
      />
    )
  }

  return <p className="step-description">{step.description}</p>
}

export function Home() {
  const { algorithms, loading: loadingAlgos, error: algosError } = useAlgorithmList()
  const runner = useAlgorithmRunner()
  const [selectedAlgo, setSelectedAlgo] = useState<Algorithm | null>(null)

  function handleSelect(algo: Algorithm) {
    setSelectedAlgo(algo)
    runner.reset()
  }

  if (loadingAlgos) return <div className="loading">Carregando algoritmos...</div>
  if (algosError) return <div className="error">Erro: {algosError}</div>

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1 className="app-title">algolab</h1>
        <AlgorithmSelector
          algorithms={algorithms}
          selectedId={selectedAlgo?.id ?? null}
          onSelect={handleSelect}
        />
      </aside>

      <main className="main-content">
        {!selectedAlgo ? (
          <div className="empty-state">
            <p>Selecione um algoritmo para começar.</p>
          </div>
        ) : (
          <>
            <div className="algo-header">
              <h2>{selectedAlgo.name}</h2>
              <p className="algo-description">{selectedAlgo.description}</p>
              <div className="complexity-badges">
                <span>Tempo: {selectedAlgo.time_complexity}</span>
                <span>Espaço: {selectedAlgo.space_complexity}</span>
              </div>
            </div>

            <InputPanel
              algorithm={selectedAlgo}
              onRun={(input) => runner.run(selectedAlgo.id, input)}
              isLoading={runner.isLoading}
            />

            {runner.error && <p className="error">{runner.error}</p>}

            {runner.result && runner.currentStep && (
              <>
                {renderVisualizer(selectedAlgo, runner.currentStep)}
                <ControlBar
                  currentIndex={runner.currentStepIndex}
                  totalSteps={runner.result.total_steps}
                  isPlaying={runner.isPlaying}
                  onPlay={() => runner.play(600)}
                  onPause={runner.pause}
                  onStepForward={runner.stepForward}
                  onStepBackward={runner.stepBackward}
                  onReset={runner.reset}
                />
              </>
            )}
          </>
        )}
      </main>
    </div>
  )
}
