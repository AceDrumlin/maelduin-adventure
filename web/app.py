#!/usr/bin/env python3
"""The Voyage of Mael Duin - Web Edition (zero dependencies, built-in http.server)"""

import sys
import os
import json
import uuid
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from game.engine import GameState, process_command, handle_look

# Import world data to register locations
from game import world  # noqa: F401

# In-memory game sessions
game_states = {}

# HTML template (embedded to avoid needing a template engine)
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Voyage of Mael Duin</title>
    <style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0f;color:#c8d6e5;font-family:'Courier New',monospace;height:100vh;overflow:hidden}
#game{display:flex;flex-direction:column;height:100vh;max-width:900px;margin:0 auto}
#header{padding:10px 20px 5px;border-bottom:1px solid #2c3e50;flex-shrink:0;text-align:center}
#ascii-title{color:#f0c040;font-size:10px;line-height:1.1;margin-bottom:5px}
#status-bar{display:flex;justify-content:space-between;font-size:13px;color:#2c3e50;padding:4px 0;border-top:1px solid #2c3e50;margin-top:4px}
#output{flex:1;overflow-y:auto;padding:15px 20px;white-space:pre-wrap;word-wrap:break-word;line-height:1.5;font-size:14px;scroll-behavior:smooth}
#output::-webkit-scrollbar{width:6px}
#output::-webkit-scrollbar-track{background:#0a0a0f}
#output::-webkit-scrollbar-thumb{background:#2c3e50;border-radius:3px}
#input-area{display:flex;padding:10px 20px;border-top:1px solid #2c3e50;gap:8px;flex-shrink:0}
#prompt{color:#f0c040;font-weight:bold;font-size:16px;line-height:40px}
#cmd{flex:1;background:#0d0d1a;border:1px solid #2c3e50;color:#c8d6e5;font-family:'Courier New',monospace;font-size:15px;padding:10px 14px;border-radius:4px;outline:none}
#cmd:focus{border-color:#f0c040}
#send{background:#f0c040;color:#0a0a0f;border:none;padding:10px 20px;font-size:16px;border-radius:4px;cursor:pointer;font-weight:bold}
#send:hover{background:#e0b030}
.msg{animation:fadeIn .3s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.loc{color:#f0c040;font-weight:bold}
.sys{color:#5fad5f;font-style:italic}
.err{color:#c0392b}
#inventory{position:fixed;top:10px;right:10px;background:#1a1a2e;border:1px solid #2c3e50;padding:12px;border-radius:4px;font-size:12px;max-width:220px;z-index:10}
#inventory h3{color:#f0c040;margin-bottom:6px;font-size:11px;letter-spacing:1px;text-transform:uppercase}
#inventory ul{list-style:none}
#inventory li{padding:2px 0;border-bottom:1px solid rgba(255,255,255,.05)}
@media(max-width:600px){#ascii-title{font-size:6px}#output{font-size:13px;padding:10px}}
    </style>
</head>
<body>
<div id="game">
    <div id="header">
        <pre id="ascii-title">
  _______ _   _  ___    _   ___   __
 |__   __| | | || _ \  / | /_\ \ / /
    | |  | |_| ||  _/  | |/ _ \ V /
    |_|   \___/ |_|    |_/_/ \_\_/

    The Voyage of Mael Duin
        </pre>
        <div id="status-bar">
            <span id="loc-display">Location: —</span>
            <span id="score-display">Score: 0</span>
            <span id="turn-display">Turn: 0</span>
        </div>
    </div>
    <div id="output">Loading...</div>
    <div id="input-area">
        <span id="prompt">&gt;</span>
        <input type="text" id="cmd" autofocus placeholder="Type a command...">
        <button id="send" onclick="sendCmd()" disabled>→</button>
    </div>
</div>
<div id="inventory">
    <h3>🧳 Inventory</h3>
    <ul id="inv-list"><li>Empty</li></ul>
    <button onclick="restart()" style="margin-top:10px;background:transparent;border:1px solid #c0392b;color:#c0392b;font-family:'Courier New',monospace;padding:6px 10px;border-radius:4px;cursor:pointer;width:100%;font-size:12px">🔄 New Voyage</button>
</div>
<script>
let gameOver = false;
const output = document.getElementById('output');
const cmd = document.getElementById('cmd');
const sendBtn = document.getElementById('send');
const invList = document.getElementById('inv-list');
const locDisplay = document.getElementById('loc-display');
const scoreDisplay = document.getElementById('score-display');
const turnDisplay = document.getElementById('turn-display');

function scrollBottom() { setTimeout(() => output.scrollTop = output.scrollHeight, 30) }

function addMsg(text, cls='') {
    const div = document.createElement('div');
    div.className = 'msg' + (cls ? ' ' + cls : '');
    div.textContent = text;
    output.appendChild(div);
    scrollBottom();
}

function updateUI(data) {
    locDisplay.textContent = 'Location: ' + (data.location || '?').replace(/_/g,' ').replace(/\b\w/g,c=>c.toUpperCase());
    scoreDisplay.textContent = 'Score: ' + (data.score ?? 0);
    turnDisplay.textContent = 'Turn: ' + (data.turns ?? 0);
    invList.innerHTML = '';
    if (data.inventory && data.inventory.length) {
        data.inventory.forEach(i => { const li = document.createElement('li'); li.textContent = '▸ ' + i; invList.appendChild(li) });
    } else {
        invList.innerHTML = '<li style="color:#555">Empty</li>';
    }
    gameOver = data.game_over || false;
    cmd.disabled = gameOver;
    sendBtn.disabled = gameOver;
    cmd.placeholder = gameOver ? 'Game over. New Voyage to restart.' : 'Type a command...';
}

async function sendCmd() {
    const text = cmd.value.trim();
    if (!text || gameOver) return;
    cmd.value = '';
    addMsg('> ' + text, 'sys');
    try {
        const r = await fetch('/api/command', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({command:text}) });
        const d = await r.json();
        if (d.restart) { output.innerHTML = ''; }
        addMsg(d.output || '');
        updateUI(d);
    } catch(e) { addMsg('⚠ Connection error: ' + e.message, 'err') }
}

async function restart() {
    if (!confirm('Start a new voyage? All progress will be lost.')) return;
    output.innerHTML = '';
    gameOver = false;
    try {
        const r = await fetch('/api/start', { method:'POST' });
        const d = await r.json();
        addMsg(d.output || 'Your voyage begins...');
        updateUI(d);
        cmd.focus();
    } catch(e) { addMsg('⚠ Error: ' + e.message, 'err') }
}

cmd.addEventListener('keydown', e => { if(e.key==='Enter') sendCmd() });

// Auto-start
(async () => {
    try {
        const r = await fetch('/api/start', { method:'POST' });
        const d = await r.json();
        addMsg(d.output || 'Your voyage begins...');
        updateUI(d);
        cmd.focus();
    } catch(e) { addMsg('⚠ Could not start game. Is the server running?', 'err') }
})();
</script>
</body>
</html>"""


class GameHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the Mael Duin web game."""

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._send_cors()
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html, status=200):
        body = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._send_cors()
        self.end_headers()
        self.wfile.write(body)

    def _send_static(self, filepath):
        ext = os.path.splitext(filepath)[1]
        content_type, _ = mimetypes.guess_type(filepath)
        if not content_type:
            content_type = "application/octet-stream"
        try:
            with open(filepath, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self._send_cors()
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self._send_json({"error": "File not found"}, 404)

    def _send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _get_session_id(self):
        """Get or create a session ID from cookies."""
        cookies = self.headers.get("Cookie", "")
        for c in cookies.split(";"):
            c = c.strip()
            if c.startswith("session="):
                return c[8:]
        sid = str(uuid.uuid4())
        self._set_session_cookie = sid
        return sid

    def _set_cookie(self, sid):
        self.send_header("Set-Cookie", f"session={sid}; Path=/; HttpOnly; SameSite=Lax")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self._send_html(HTML_TEMPLATE)
        elif path == "/api/state":
            sid = self._get_session_id()
            state = self._get_state(sid)
            if state:
                self._send_json(self._state_to_json(state))
            else:
                self._send_json({"error": "No game session"}, 400)
        else:
            # Try static files
            static_path = os.path.join(os.path.dirname(__file__), "static", path.lstrip("/"))
            if os.path.isfile(static_path):
                self._send_static(static_path)
            else:
                self._send_json({"error": "Not found"}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/start":
            sid = self._get_session_id()
            state = GameState()
            game_states[sid] = state
            output = handle_look(state, [])
            self.send_response(200)
            self._send_cors()
            self._set_cookie(sid)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            data = self._state_to_json(state, output)
            self.wfile.write(json.dumps(data).encode("utf-8"))
            return

        elif path == "/api/command":
            sid = self._get_session_id()
            state = game_states.get(sid)
            if not state:
                self._send_json({"error": "No game session. Start a new game."}, 400)
                return

            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length) if content_length else b"{}"
            data = json.loads(body)
            cmd = data.get("command", "").strip()

            if not cmd:
                self._send_json({"error": "Empty command."}, 400)
                return

            result = process_command(state, cmd)

            if result == "__RESTART__":
                # Restart game
                new_state = GameState()
                game_states[sid] = new_state
                output = handle_look(new_state, [])
                data = self._state_to_json(new_state, output)
                data["restart"] = True
                self._send_json(data)
                return

            self.send_response(200)
            self._send_cors()
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            resp_data = self._state_to_json(state, result)
            self.wfile.write(json.dumps(resp_data).encode("utf-8"))
            return

        self._send_json({"error": "Not found"}, 404)

    def _get_state(self, sid):
        return game_states.get(sid)

    def _state_to_json(self, state, output=None):
        return {
            "output": output or "",
            "location": state.current_location,
            "inventory": [i.name for i in state.inventory],
            "score": state.score,
            "turns": state.turns,
            "game_over": state.game_over,
            "won": state.won,
        }


def main():
    port = int(os.environ.get("PORT", 5000))
    server = HTTPServer(("0.0.0.0", port), GameHandler)
    print(f"\n  🌊 The Voyage of Mael Duin — Web Edition")
    print(f"  📖 Open http://localhost:{port} in your browser")
    print(f"  ⚓ Press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nFarewell, voyager!")
        server.server_close()


if __name__ == "__main__":
    main()
