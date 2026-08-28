import { Link } from "react-router-dom"

function Informations() {
  return (
    <main className="info-page">

      <div className="badge">● ABOUT THE TOOL</div>

      <h1 className="info-title">Informations</h1>

      <p className="info-intro">
        Welcome to the information page.
      </p>

      <section className="info-card">
        <h2>Network Security Testing</h2>

        <p>
          This tool is designed for network security testing and penetration
          testing. It combines different types of network security tests for
          educational and authorized environments.
        </p>

        <h3>Available Modules</h3>

        <ul className="attack-list">
          <li>ARP Spoofing</li>
          <li>Packet Sniffing</li>
          <li>DoS Testing</li>
          <li>WPS Security Testing</li>
          <li>Deauthentication Testing</li>
        </ul>
      </section>

      <section className="info-card">
        <h2>About The Project</h2>

        <p>
          This tool is designed for Kali Linux and is built as a Python project.
          You can modify the source code and add new features to experiment
          with network security concepts.
        </p>

        <p>
          The project is intended for educational and authorized security
          testing only. Do not use it against systems or networks without
          permission.
        </p>
      </section>

      <section className="install-section">
        <h2>Ready to get started?</h2>

        <p>
          Install the tool and start learning about network security.
        </p>

        <Link className="install-link" to="/install-the-tool">
          Install It Now →
        </Link>
      </section>

    </main>
  )
}

export default Informations