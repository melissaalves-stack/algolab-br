// Hook central: executa um algoritmo e controla a animação passo a passo.
// Expõe: os passos, o passo atual, se está rodando, e os controles (play/pause/step).

import { useState, useRef, useCallback } from "react"
import type { ExecutionResult, ExecutionStep } from "@/domain/Algorithm"
import { executeAlgorithm } from "@/adapters/api/algorithmApi"

interface RunnerState {
  result: ExecutionResult | null
  currentStepIndex: number
  isPlaying: boolean
  isLoading: boolean
  error: string | null
}

export function useAlgorithmRunner() {
  const [state, setState] = useState<RunnerState>({
    result: null,
    currentStepIndex: 0,
    isPlaying: false,
    isLoading: false,
    error: null,
  })

  // useRef guarda o intervalo do play sem provocar re-render
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)

  const currentStep: ExecutionStep | null =
    state.result?.steps[state.currentStepIndex] ?? null

  // Busca os passos da API e reseta o estado de animação
  const run = useCallback(async (algorithmId: string, inputData: unknown) => {
    clearInterval(intervalRef.current!)
    setState(prev => ({ ...prev, isLoading: true, error: null, isPlaying: false, currentStepIndex: 0 }))
    try {
      const result = await executeAlgorithm(algorithmId, inputData)
      setState(prev => ({ ...prev, result, isLoading: false }))
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : "Erro desconhecido."
      setState(prev => ({ ...prev, isLoading: false, error: message }))
    }
  }, [])

  // Avança um passo manualmente
  const stepForward = useCallback(() => {
    setState(prev => {
      if (!prev.result) return prev
      const next = Math.min(prev.currentStepIndex + 1, prev.result.steps.length - 1)
      return { ...prev, currentStepIndex: next }
    })
  }, [])

  // Volta um passo manualmente
  const stepBackward = useCallback(() => {
    setState(prev => ({
      ...prev,
      currentStepIndex: Math.max(prev.currentStepIndex - 1, 0),
    }))
  }, [])

  // Inicia a reprodução automática — avança um passo a cada `speed` ms
  const play = useCallback((speed: number = 600) => {
    setState(prev => ({ ...prev, isPlaying: true }))
    intervalRef.current = setInterval(() => {
      setState(prev => {
        if (!prev.result) return prev
        const isLast = prev.currentStepIndex >= prev.result.steps.length - 1
        if (isLast) {
          clearInterval(intervalRef.current!)
          return { ...prev, isPlaying: false }
        }
        return { ...prev, currentStepIndex: prev.currentStepIndex + 1 }
      })
    }, speed)
  }, [])

  const pause = useCallback(() => {
    clearInterval(intervalRef.current!)
    setState(prev => ({ ...prev, isPlaying: false }))
  }, [])

  const reset = useCallback(() => {
    clearInterval(intervalRef.current!)
    setState(prev => ({ ...prev, currentStepIndex: 0, isPlaying: false }))
  }, [])

  return {
    ...state,
    currentStep,
    run,
    play,
    pause,
    reset,
    stepForward,
    stepBackward,
  }
}
