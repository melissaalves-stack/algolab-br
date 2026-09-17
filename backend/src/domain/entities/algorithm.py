# Representa um algoritmo disponível no sistema.
# Essa classe é puro dado — sem lógica, sem framework.
# Qualquer parte do sistema que precisar falar sobre um algoritmo usa isso aqui.

from dataclasses import dataclass


@dataclass(frozen=True)
class Algorithm:
    id: str           # ex: "bubble_sort"
    name: str         # ex: "Bubble Sort"
    category: str     # ex: "array", "graph", "tree"
    description: str
    time_complexity: str   # ex: "O(n²)"
    space_complexity: str  # ex: "O(1)"
