app.py - Flask backend to serve the HTML emulator dashboard

from flask import Flask, send_file import os

app = Flask(name)

@app.route("/") def home(): return send_file("dashboard.html")

if name == "main": app.run(debug=True, host="0.0.0.0", port=5000)

<!-- dashboard.html (place this file in the same directory as app.py) --><!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>kader11000 Emulator Control</title>
  <style>
    body {
      margin: 0;
      font-family: 'Courier New', monospace;
      background: #0f0f0f;
      color: #e0e0e0;
    }
    header {
      background: #111;
      padding: 1rem;
      text-align: center;
      font-size: 1.5rem;
      font-weight: bold;
      color: #00ffc3;
      box-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }
    .shortcuts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      background: #1a1a1a;
      padding: 1rem;
      position: sticky;
      top: 0;
      z-index: 1000;
    }
    .shortcut-btn {
      background: #222;
      border: 1px solid #444;
      color: #0f0;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      cursor: pointer;
      transition: 0.2s;
    }
    .shortcut-btn:hover {
      background: #0f0;
      color: #000;
    }
    .emulator-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      padding: 1rem;
      justify-content: center;
    }
    .emulator {
      background: #1e1e1e;
      padding: 1rem;
      border-radius: 8px;
      width: 350px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    iframe {
      width: 100%;
      height: 500px;
      border: 1px solid #333;
      border-radius: 6px;
    }
    .control-panel {
      margin-top: 1rem;
      background: #111;
      padding: 0.5rem;
      border-radius: 6px;
    }
    .terminal {
      background: #000;
      color: #0f0;
      padding: 0.5rem;
      margin-top: 0.5rem;
      font-size: 0.85rem;
      height: 120px;
      overflow-y: auto;
      border-radius: 4px;
      position: relative;
    }
    .terminal-input {
      width: 100%;
      border: none;
      background: transparent;
      color: #0f0;
      outline: none;
      font-family: inherit;
    }
    .control-btn {
      background: #333;
      color: #0f0;
      border: none;
      padding: 5px 10px;
      border-radius: 4px;
      margin: 5px 3px;
      cursor: pointer;
      font-size: 0.85rem;
    }
    .control-btn:hover {
      background: #0f0;
      color: #000;
    }
  </style>
</head>
<body>
  <header>KADER11000 Emulator Dashboard</header>  <div class="shortcuts">
    <button class="shortcut-btn" onclick="launchToAll('exp://u.expo.dev/tiktok-clone-demo')">TikTok Clone</button>
    <button class="shortcut-btn" onclick="launchToAll('exp://u.expo.dev/instagram-ui-demo')">Instagram UI</button>
    <button class="shortcut-btn" onclick="launchToAll('exp://u.expo.dev/snapchat-clone')">Snapchat</button>
    <button class="shortcut-btn" onclick="launchToAll('exp://u.expo.dev/youtube-ui-clone')">YouTube UI</button>
  </div>  <div class="emulator-container" id="emulators"></div>  <script>
    const baseURL = "https://appetize.io/embed/b_vfyableb3rimkjc4gfht7aqrn4?device=pixel8&scale=auto&orientation=portrait&centered=both";

    function createEmulator(index) {
      const container = document.createElement('div');
      container.className = 'emulator';
      container.innerHTML = `
        <iframe src="${baseURL}&launchUrl=" id="iframe-${index}"></iframe>
        <div class="control-panel">
          <button class="control-btn" onclick="launchApp(${index})">Launch</button>
          <button class="control-btn" onclick="installApp(${index})">Install App</button>
          <button class="control-btn" onclick="resetEmulator(${index})">Reset</button>
          <div class="terminal" id="terminal-${index}">
            <div>>> Terminal ready</div>
          </div>
          <input class="terminal-input" type="text" placeholder="type command..." onkeydown="handleCommand(event, ${index})" />
        </div>
      `;
      return container;
    }

    function launchApp(index) {
      logToTerminal(index, 'Launching application...');
    }
    function installApp(index) {
      logToTerminal(index, 'Installing app...');
    }
    function resetEmulator(index) {
      logToTerminal(index, 'Resetting emulator...');
    }
    function handleCommand(e, index) {
      if (e.key === 'Enter') {
        const cmd = e.target.value;
        logToTerminal(index, `> ${cmd}`);
        e.target.value = '';
        setTimeout(() => logToTerminal(index, fakeResponse(cmd)), 300);
      }
    }
    function fakeResponse(cmd) {
      switch (cmd.toLowerCase()) {
        case 'launch': return 'Launching app... Done.';
        case 'status': return 'Emulator online. App running.';
        case 'login': return 'Sending credentials... Success';
        case 'clear': return '';
        default: return `Command not found: ${cmd}`;
      }
    }
    function logToTerminal(index, text) {
      const term = document.getElementById(`terminal-${index}`);
      if (text === '') term.innerHTML = '';
      else term.innerHTML += `<div>${text}</div>`;
      term.scrollTop = term.scrollHeight;
    }
    function launchToAll(url) {
      for (let i = 0; i < 10; i++) {
        const iframe = document.getElementById(`iframe-${i}`);
        iframe.src = `${baseURL}&launchUrl=${encodeURIComponent(url)}`;
        logToTerminal(i, `Launching ${url}`);
      }
    }

    const emulators = document.getElementById('emulators');
    for (let i = 0; i < 10; i++) {
      emulators.appendChild(createEmulator(i));
    }
  </script></body>
</html>
