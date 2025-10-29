FROM node:22-alpine

WORKDIR /app

# Ferramentas de compilação necessárias para npm
RUN apk add --no-cache python3 make g++

COPY package*.json ./
RUN npm install

COPY . .

# Build do Vue dentro do container
RUN npm run build

RUN npm install -g serve

EXPOSE 8080

# Serve SPA com --single para todas as rotas
CMD ["serve", "-s", "dist", "-l", "8080", "--single"]
