import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import './index.css'

import App from './App.tsx'
import Informations from './informations.tsx'
import InstallTheTool from './install_the_tool.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/informations" element={<Informations />} />
        <Route path="/install-the-tool" element={<InstallTheTool />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)