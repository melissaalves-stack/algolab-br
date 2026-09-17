// Configuração do Vite: define o plugin React e o alias @/ para src/
// O alias permite escrever "@/components/..." em vez de "../../components/..."

import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import { resolve } from "path"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    },
  },
})
