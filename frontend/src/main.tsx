// Ponto de entrada da aplicação React.
// O Vite procura esse arquivo automaticamente.

import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { Home } from "@/pages/Home"
import "./index.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Home />
  </StrictMode>,
)
