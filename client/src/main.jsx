import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { EpisodeProvider } from './contexts/EpisodeContext';
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <EpisodeProvider>
        <App />
      </EpisodeProvider>
    </BrowserRouter>
  </React.StrictMode>,
)
