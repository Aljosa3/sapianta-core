"""Static institutional homepage for Product 1."""

from fastapi.responses import HTMLResponse


def enterprise_demo_html() -> HTMLResponse:
    return HTMLResponse(
        """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SAPIANTA - AI Decision Validator</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #040b14;
      --bg-deep: #020712;
      --text: #e8e8e4;
      --muted: #aaa8a2;
      --faint: #6f777b;
      --line: rgba(224, 225, 217, 0.42);
      --line-soft: rgba(224, 225, 217, 0.24);
      --green: #9fbe78;
      --green-line: rgba(159, 190, 120, 0.55);
    }

    * { box-sizing: border-box; }

    html,
    body {
      min-height: 100%;
    }

    body {
      margin: 0;
      background:
        radial-gradient(circle at 72% 54%, rgba(21, 46, 65, 0.24), transparent 30%),
        radial-gradient(circle at 8% 50%, rgba(24, 47, 62, 0.18), transparent 34%),
        linear-gradient(90deg, var(--bg-deep), var(--bg) 22%, #06111c 64%, var(--bg-deep));
      color: var(--text);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.45;
      overflow-x: hidden;
    }

    a { color: inherit; }

    .page {
      position: relative;
      min-height: 100vh;
      isolation: isolate;
    }

    .page::before {
      content: "";
      position: absolute;
      inset: 0;
      z-index: -1;
      background:
        linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px),
        linear-gradient(180deg, rgba(255,255,255,0.012) 1px, transparent 1px);
      background-size: 148px 148px;
      opacity: 0.34;
      mask-image: linear-gradient(90deg, transparent 0%, black 12%, black 82%, transparent 100%);
    }

    .shell {
      width: min(1240px, calc(100% - 96px));
      margin: 0 auto;
    }

    .topbar {
      height: 150px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      padding-top: 26px;
    }

    .brand {
      width: 156px;
      color: var(--text);
    }

    .brand img {
      display: block;
      width: 126px;
      height: 126px;
      object-fit: contain;
    }

    .nav {
      display: flex;
      align-items: center;
      gap: 28px;
      padding-top: 4px;
      color: #d2d0ca;
      font-size: 13px;
      font-weight: 430;
    }

    .nav-toggle,
    .nav-trigger {
      display: none;
    }

    .nav a {
      text-decoration: none;
      opacity: 0.88;
    }

    .nav a:hover {
      opacity: 1;
    }

    .demo-button {
      margin-left: 12px;
      min-width: 124px;
      height: 42px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--green-line);
      border-radius: 6px;
      color: var(--green);
      background: rgba(159, 190, 120, 0.025);
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(390px, 0.78fr) minmax(640px, 1.22fr);
      gap: 56px;
      align-items: center;
      min-height: calc(100vh - 150px);
      padding: 40px 0 94px;
    }

    .copy {
      align-self: center;
      padding-top: 12px;
    }

    h1 {
      margin: 0;
      max-width: 520px;
      font-size: clamp(63px, 7vw, 86px);
      line-height: 1.04;
      letter-spacing: -0.02em;
      font-weight: 720;
      color: #eeeeea;
      text-shadow: 0 14px 30px rgba(0, 0, 0, 0.5);
    }

    .subtitle {
      margin: 22px 0 0;
      color: var(--muted);
      font-size: 24px;
      font-weight: 360;
      letter-spacing: -0.01em;
    }

    .eu-note {
      margin-top: 50px;
      max-width: 330px;
      border-top: 1px solid var(--green-line);
      padding-top: 28px;
      display: grid;
      grid-template-columns: 72px 1fr;
      gap: 28px;
      align-items: center;
    }

    .eu-stars {
      position: relative;
      width: 58px;
      height: 58px;
    }

    .eu-stars span {
      position: absolute;
      left: 50%;
      top: 50%;
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #d7d3c9;
      transform: rotate(calc(var(--i) * 30deg)) translateY(-25px);
      transform-origin: 0 0;
    }

    .eu-title {
      margin-bottom: 8px;
      color: #e5e2db;
      font-size: 14px;
      letter-spacing: 0.18em;
      font-weight: 560;
    }

    .eu-copy {
      color: var(--muted);
      font-size: 16px;
      line-height: 1.48;
    }

    .pipeline-wrap {
      align-self: center;
      justify-self: stretch;
      transform: translateY(8px);
    }

    .pipeline {
      width: 100%;
      min-height: 280px;
      display: grid;
      grid-template-columns: repeat(5, minmax(104px, 1fr));
      column-gap: 36px;
      align-items: start;
      position: relative;
      padding: 0 16px 0 8px;
    }

    .pipeline::before {
      content: "";
      position: absolute;
      left: 8.5%;
      right: 8.5%;
      top: 89px;
      height: 1px;
      background: var(--line);
      z-index: 0;
    }

    .flow-item {
      position: relative;
      min-width: 0;
      text-align: center;
      z-index: 1;
    }

    .stage-label {
      height: 30px;
      margin-bottom: 16px;
      color: #d4d0ca;
      font-size: 16px;
      font-weight: 400;
    }

    .node {
      width: 86px;
      height: 86px;
      margin: 0 auto 18px;
      display: grid;
      place-items: center;
      border: 1px solid rgba(224, 225, 217, 0.28);
      border-radius: 7px;
      background: #06111c;
    }

    .node.certified {
      border-color: rgba(159, 190, 120, 0.68);
      background: #07130f;
    }

    .node svg {
      width: 48px;
      height: 48px;
      stroke: #d9d4ca;
      fill: none;
      stroke-width: 1.35;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .node.certified svg {
      stroke: #e0ded7;
    }

    .node-title {
      min-height: 48px;
      color: #dcd8d0;
      font-size: 16px;
      line-height: 1.34;
      font-weight: 420;
    }

    .status {
      color: var(--green);
      font-size: 15px;
      letter-spacing: 0.04em;
      font-weight: 500;
    }

    @media (max-width: 1180px) {
      .shell {
        width: min(100% - 54px, 1080px);
      }

      .hero {
        grid-template-columns: 1fr;
        gap: 58px;
        padding-top: 28px;
      }

      h1 {
        max-width: 720px;
        font-size: clamp(58px, 10vw, 84px);
      }

      .pipeline-wrap {
        transform: none;
      }
    }

    @media (max-width: 760px) {
      body {
        background: linear-gradient(180deg, #040b14, #07101a 58%, #020712);
      }

      .shell {
        width: min(100% - 34px, 680px);
      }

      .topbar {
        height: auto;
        padding-top: 20px;
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 20px;
        position: relative;
      }

      .brand {
        width: 118px;
      }

      .brand img {
        width: 108px;
        height: 108px;
      }

      .nav-trigger {
        width: 42px;
        height: 42px;
        margin-top: 28px;
        display: grid;
        place-items: center;
        border: 1px solid rgba(224, 225, 217, 0.22);
        border-radius: 4px;
        background: rgba(6, 17, 28, 0.72);
      }

      .nav-trigger span,
      .nav-trigger::before,
      .nav-trigger::after {
        content: "";
        width: 18px;
        height: 1px;
        background: rgba(232, 232, 228, 0.78);
      }

      .nav-trigger::before {
        transform: translateY(5px);
      }

      .nav-trigger::after {
        transform: translateY(-5px);
      }

      .nav {
        position: absolute;
        top: 92px;
        right: 0;
        width: min(284px, calc(100vw - 34px));
        display: none;
        padding: 16px;
        border: 1px solid rgba(224, 225, 217, 0.16);
        background: #06111c;
        gap: 0;
        flex-direction: column;
        align-items: stretch;
        font-size: 12px;
        z-index: 10;
      }

      .nav-toggle:checked ~ .nav {
        display: flex;
      }

      .nav a {
        min-height: 38px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid rgba(224, 225, 217, 0.08);
      }

      .nav a:last-child {
        border-bottom: 0;
      }

      .demo-button {
        margin: 12px 0 0;
        width: 100%;
        min-width: 0;
        padding: 0 18px;
      }

      .hero {
        min-height: auto;
        padding: 64px 0 70px;
      }

      h1 {
        font-size: clamp(52px, 16vw, 72px);
      }

      .subtitle {
        font-size: 20px;
      }

      .eu-note {
        margin-top: 48px;
      }

      .pipeline {
        grid-template-columns: 1fr;
        gap: 28px;
        padding: 8px 0 2px;
      }

      .pipeline::before {
        display: block;
        left: 144px;
        right: auto;
        top: 58px;
        bottom: 42px;
        width: 1px;
        height: auto;
      }

      .flow-item {
        display: grid;
        grid-template-columns: 84px 72px minmax(0, 1fr) 76px;
        column-gap: 24px;
        align-items: center;
        text-align: left;
      }

      .flow-item:last-child {
        margin-top: 0;
        padding-top: 0;
      }

      .stage-label {
        height: auto;
        margin-bottom: 0;
        text-align: right;
        white-space: nowrap;
      }

      .node {
        width: 72px;
        height: 72px;
        margin: 0;
      }

      .node svg {
        width: 38px;
        height: 38px;
      }

      .node-title {
        min-height: 0;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <header class="topbar shell">
      <a class="brand" href="/" aria-label="SAPIANTA home">
        <img src="/static/img/sapianta-logo-white.png" alt="SAPIANTA">
      </a>

      <input class="nav-toggle" id="nav-toggle" type="checkbox" aria-label="Toggle navigation">
      <label class="nav-trigger" for="nav-toggle" aria-hidden="true"><span></span></label>

      <nav class="nav" aria-label="Primary">
        <a href="#platform">Platform</a>
        <a href="#governance">Governance</a>
        <a href="#runtime">Runtime</a>
        <a href="#compliance">Compliance</a>
        <a href="/docs">Audit</a>
        <a href="#contact">Contact</a>
        <a class="demo-button" href="#contact">Request Demo</a>
      </nav>
    </header>

    <main class="hero shell">
      <section class="copy" aria-labelledby="hero-title">
        <h1 id="hero-title">AI Decision<br>Validator</h1>
        <p class="subtitle">Govern AI execution before runtime.</p>

        <div class="eu-note" aria-label="EU AI Act aligned">
          <div class="eu-stars" aria-hidden="true">
            <span style="--i:0"></span><span style="--i:1"></span><span style="--i:2"></span>
            <span style="--i:3"></span><span style="--i:4"></span><span style="--i:5"></span>
            <span style="--i:6"></span><span style="--i:7"></span><span style="--i:8"></span>
            <span style="--i:9"></span><span style="--i:10"></span><span style="--i:11"></span>
          </div>
          <div>
            <div class="eu-title">EU AI ACT ALIGNED</div>
            <div class="eu-copy">Structured governance for trustworthy AI systems.</div>
          </div>
        </div>
      </section>

      <section class="pipeline-wrap" aria-label="Governance validation pipeline">
        <div class="pipeline">
          <article class="flow-item" id="platform">
            <div class="stage-label">AI</div>
            <div class="node" aria-hidden="true">
              <svg viewBox="0 0 48 48">
                <circle cx="24" cy="8" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="16" cy="14" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="24" cy="14" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="32" cy="14" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="10" cy="22" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="18" cy="22" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="30" cy="22" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="38" cy="22" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="16" cy="30" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="24" cy="30" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="32" cy="30" r="1.6" fill="currentColor" stroke="none"/>
                <circle cx="24" cy="38" r="1.6" fill="currentColor" stroke="none"/>
              </svg>
            </div>
            <div class="node-title">AI Decision</div>
            <div class="status">PASS</div>
          </article>

          <article class="flow-item" id="governance">
            <div class="stage-label">M1</div>
            <div class="node" aria-hidden="true">
              <svg viewBox="0 0 48 48">
                <path d="M14 16l2 2 4-5"/>
                <path d="M26 16h12"/>
                <path d="M14 24l2 2 4-5"/>
                <path d="M26 24h12"/>
                <circle cx="16" cy="34" r="2.2"/>
                <path d="M26 34h12"/>
              </svg>
            </div>
            <div class="node-title">Correctness Gate</div>
            <div class="status">PASS</div>
          </article>

          <article class="flow-item" id="compliance">
            <div class="stage-label">M2</div>
            <div class="node" aria-hidden="true">
              <svg viewBox="0 0 48 48">
                <path d="M24 7l17 7v10c0 9-7 15-17 18C14 39 7 33 7 24V14l17-7z"/>
                <path d="M16 24l6 6 12-14"/>
              </svg>
            </div>
            <div class="node-title">Policy Validation</div>
            <div class="status">PASS</div>
          </article>

          <article class="flow-item execution" id="runtime">
            <div class="stage-label">M3</div>
            <div class="node" aria-hidden="true">
              <svg viewBox="0 0 48 48">
                <rect x="11" y="21" width="26" height="20"/>
                <path d="M17 21v-7a7 7 0 0 1 14 0v7"/>
              </svg>
            </div>
            <div class="node-title">Execution Safety</div>
            <div class="status">PASS</div>
          </article>

          <article class="flow-item">
            <div class="stage-label status">CERTIFIED</div>
            <div class="node certified" aria-hidden="true">
              <svg viewBox="0 0 48 48">
                <circle cx="24" cy="24" r="19"/>
                <path d="M15 25l6 6 13-15"/>
              </svg>
            </div>
            <div class="node-title">Deterministic<br>Audit</div>
            <div class="status">CERTIFIED</div>
          </article>
        </div>
      </section>
    </main>
  </div>
</body>
</html>
        """.strip()
    )
