function InstallTheTool() {
  return (
    <main className="install-page">

      <div className="badge">● INSTALLATION</div>

      <h1 className="welcome">Install The Tool</h1>

      <p className="description">
        Download HackerX and start your cybersecurity learning journey.
      </p>

      <div className="install-card">

        <h2>HackerX</h2>

        <p>
          Download the latest version of HackerX and extract the files
          on your Kali Linux system.
        </p>

        <a
          className="install-link"
          href="/HackerX.zip"
          download
        >
          Download HackerX →
        </a>

      </div>

    </main>
  )
}

export default InstallTheTool