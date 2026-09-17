// Barra de controle da animação.
// Mostra o progresso e os botões de navegação de passos.

interface Props {
  currentIndex: number
  totalSteps: number
  isPlaying: boolean
  onPlay: () => void
  onPause: () => void
  onStepForward: () => void
  onStepBackward: () => void
  onReset: () => void
}

export function ControlBar({
  currentIndex,
  totalSteps,
  isPlaying,
  onPlay,
  onPause,
  onStepForward,
  onStepBackward,
  onReset,
}: Props) {
  const isAtEnd = currentIndex >= totalSteps - 1

  return (
    <div className="control-bar" role="toolbar" aria-label="Controles de animação">
      <button onClick={onReset} aria-label="Reiniciar">⟳</button>
      <button onClick={onStepBackward} disabled={currentIndex === 0} aria-label="Passo anterior">‹</button>

      {isPlaying ? (
        <button onClick={onPause} aria-label="Pausar">⏸</button>
      ) : (
        <button onClick={onPlay} disabled={isAtEnd} aria-label="Reproduzir">▶</button>
      )}

      <button onClick={onStepForward} disabled={isAtEnd} aria-label="Próximo passo">›</button>

      <span className="step-counter" aria-live="polite">
        {currentIndex + 1} / {totalSteps}
      </span>
    </div>
  )
}
