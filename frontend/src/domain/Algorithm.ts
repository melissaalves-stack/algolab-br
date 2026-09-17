// Espelha as entidades do backend em TypeScript.
// Qualquer parte do frontend que precisar falar sobre um algoritmo usa esse tipo.

export interface Algorithm {
  id: string
  name: string
  category: string
  description: string
  time_complexity: string
  space_complexity: string
}

export interface ExecutionStep {
  step_number: number
  description: string
  state: Record<string, unknown>   // varia por algoritmo
  highlighted: (number | string)[] // índices ou nomes de nós
  is_final: boolean
}

export interface ExecutionResult {
  algorithm_id: string
  total_steps: number
  steps: ExecutionStep[]
}
