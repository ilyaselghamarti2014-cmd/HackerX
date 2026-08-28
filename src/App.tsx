import { Link } from 'react-router-dom'
import { Analytics } from '@vercel/analytics/react';

function App() {
  return (
    <main className="hero-section">
      <div className="badge">● CYBER SECURITY TOOL</div>

      <h1 className="welcome">Welcome To My Tool</h1>

      <p className="description">
        Hello my name is Gosty. I am a software engineer and I have created
        this tool to help you in your cyber security journey.
        This tool is designed to help you learn cyber security.
        I hope you find this tool useful and enjoy using it!
      </p>

      <Link className="learn-more" to="/informations">
        Learn More →
      </Link>

      <Link className="install-link" to="/install-the-tool">
        Install The Tool →
      </Link>
    </main>
  )
}

export default App