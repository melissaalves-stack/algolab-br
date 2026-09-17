FROM python:3.12-slim

WORKDIR /app

# Copia as dependências primeiro para aproveitar o cache do Docker
# (só reinstala quando requirements.txt mudar)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.infrastructure.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
