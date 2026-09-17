FROM node:20-slim

WORKDIR /app

# Instala dependências antes de copiar o resto (cache do Docker)
COPY package.json .
RUN npm install

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
