# Entry point que o Vercel usa para encontrar a aplicação FastAPI.
# O Vercel procura por um objeto chamado `app` nesse arquivo.
# Aqui simplesmente reexportamos o app que já existe em src/.

import sys
import os

# Garante que o Vercel consiga importar os módulos de src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.infrastructure.api.main import app
