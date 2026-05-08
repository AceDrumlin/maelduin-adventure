#!/usr/bin/env python3
"""The Voyage of Mael Duin - Web Edition (zero dependencies)"""

import sys, os, json, uuid, mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from game.engine import GameState, process_command, handle_look
from game import world  # noqa: F401

game_states = {}

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Voyage of Mael Duin</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=MedievalSharp&family=Special+Elite&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0806;color:#c8b89a;font-family:'Special Elite','Courier New',monospace;height:100vh;height:100dvh;overflow:hidden;background-image:radial-gradient(ellipse at 20% 50%, #1a1410 0%, #0a0806 70%)}
#game{display:flex;flex-direction:column;height:100vh;height:100dvh;max-width:900px;margin:0 auto;position:relative}
#header{text-align:center;padding:6px 15px 4px;border-bottom:1px solid #2a1f14;flex-shrink:0;background:linear-gradient(180deg,#0f0b08,#0a0806)}
#title-row{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:2px}
#title-row pre{color:#b8860b;font-size:9px;line-height:1.1;text-shadow:0 0 8px rgba(184,134,11,.3)}
.celtic{color:#5a4a3a;font-size:20px;user-select:none}
#status-bar{display:flex;justify-content:space-between;font-size:11px;color:#5a4a3a;padding:3px 8px;border-top:1px solid #1a1410;font-family:'Courier New',monospace;letter-spacing:.5px}
.status-val{color:#b8860b}
#output{flex:1;min-height:0;overflow-y:auto;padding:12px 18px;white-space:pre-wrap;word-wrap:break-word;line-height:1.6;font-size:14px;scroll-behavior:smooth;color:#c8b89a}
#output::-webkit-scrollbar{width:5px}
#output::-webkit-scrollbar-track{background:#0a0806}
#output::-webkit-scrollbar-thumb{background:#2a1f14;border-radius:3px}
#input-row{display:flex;padding:8px 15px;border-top:1px solid #2a1f14;gap:6px;flex-shrink:0;background:#0f0b08}
#prompt{color:#b8860b;font-weight:bold;font-size:15px;line-height:38px;margin-right:2px}
#cmd{flex:1;background:#0d0906;border:1px solid #2a1f14;color:#c8b89a;font-family:'Special Elite','Courier New',monospace;font-size:14px;padding:8px 12px;border-radius:3px;outline:none}
#cmd:focus{border-color:#b8860b}
#cmd::placeholder{color:#3a2a1a}
#send{background:#b8860b;color:#0a0806;border:none;padding:8px 16px;font-size:15px;border-radius:3px;cursor:pointer;font-weight:bold;font-family:'Special Elite',monospace}
#send:hover{background:#d4a017}
.msg{animation:fadeIn .35s ease;padding:1px 0}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.loc{color:#b8860b;font-weight:bold;font-size:15px;text-shadow:0 0 4px rgba(184,134,11,.15)}
.npc{color:#c8a87a;font-style:italic}
.item{color:#8b7d6b}
.sys{color:#6b8e50;font-style:italic;opacity:.8}
.combat{color:#c0392b}
.humor{color:#d4a017;font-style:italic}
.err{color:#8b3a3a}
#inventory-bar{display:flex;gap:0;padding:3px 10px;background:#0d0906;border-top:1px solid #1a1410;flex-shrink:0;overflow-x:auto;font-size:11px}
#inventory-bar::-webkit-scrollbar{height:2px}
#inventory-bar::-webkit-scrollbar-thumb{background:#2a1f14}
.inv-item{background:#1a1410;border:1px solid #2a1f14;border-radius:2px;padding:2px 6px;white-space:nowrap;color:#8b7d6b;font-size:10px}
.inv-item:before{content:"\2728";margin-right:3px;font-size:8px}
#side-toggle{position:absolute;top:8px;right:12px;color:#5a4a3a;cursor:pointer;font-size:18px;z-index:20;transition:color .2s}
#side-toggle:hover{color:#b8860b}
#side-panel{position:fixed;top:0;right:-320px;width:300px;height:100vh;height:100dvh;background:#0f0b08;border-left:2px solid #2a1f14;padding:50px 18px 20px;transition:right .3s ease;overflow-y:auto;z-index:19}
#side-panel.open{right:0}
#side-panel h3{color:#b8860b;font-size:12px;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;border-bottom:1px solid #1a1410;padding-bottom:4px}
#score-detail{margin:12px 0;font-size:12px;color:#5a4a3a}
#score-detail span{color:#c8b89a}
#crew-list{list-style:none;font-size:12px}
#crew-list li{padding:3px 0;display:flex;align-items:center;gap:6px}
#crew-list li:before{content:"\1F9DD";font-size:14px}
#crew-list .dead{opacity:.4;text-decoration:line-through}
#crew-list .dead:before{content:"\1F480";font-size:14px}
#restart-btn{display:block;width:100%;margin-top:16px;padding:8px;background:transparent;border:1px solid #4a2a1a;color:#8b3a3a;font-family:'Special Elite',monospace;font-size:13px;border-radius:3px;cursor:pointer;transition:all .2s}
#restart-btn:hover{background:#4a2a1a;color:#c0392b}
.backdrop{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.5);z-index:18;display:none}
.backdrop.show{display:block}
@media(max-width:600px){
  #header{padding:2px 0!important}
  #title-row pre{display:none!important}
  .celtic{display:none!important}
  #title-row{min-height:0!important;padding:0!important}
  #status-bar{font-size:11px!important;padding:2px 6px!important}
  #status-bar span{font-size:11px!important}
  #output{font-size:15px!important;padding:6px 10px!important}
  #inventory-bar{min-height:20px!important;padding:2px 6px!important}
  .inv-item{font-size:10px!important;padding:1px 4px!important}
  #input-row{padding:6px 8px!important}
  #cmd{font-size:16px!important;padding:8px 10px!important}
  #send{font-size:14px!important;padding:8px 14px!important}
  #prompt{font-size:16px!important;line-height:36px!important}
  #side-panel{width:260px!important;right:-280px!important}
}
  .celtic{display:none}
  #title-row{min-height:0;padding:0;height:0}
  #header{padding:0;border-bottom-width:0}
  #status-bar{font-size:8px;padding:1px 4px}
  #status-bar span{font-size:8px}
  #output{font-size:12px;padding:4px 8px}
  #inventory-bar{min-height:0;padding:1px 4px}
  #inventory-bar .inv-item{font-size:8px;padding:0 3px}
  #input-row{padding:3px 6px}
  #cmd{font-size:12px;padding:4px 6px}
  #side-panel{width:240px;right:-260px}
  #prompt{font-size:12px;line-height:28px}
  #send{font-size:11px;padding:4px 8px}
}
@media(max-width:380px){
  #status-bar span{font-size:8px}
  #prompt{font-size:12px;line-height:30px}
  #input-row{padding:4px 6px}
}
</style>
</head>
<body>
<div id="game">
<div id="header">
<div id="title-row">
<span class="celtic">&#9763;</span>
<pre>
  _______ _   _  ___    _   ___   __
 |__   __| | | || _ \  / | /_\ \ / /
    | |  | |_| ||  _/  | |/ _ \ V /
    |_|   \___/ |_|    |_/_/ \_\_/
</pre>
<span class="celtic">&#9763;</span>
</div>
<div id="status-bar">
<span>LOC: <span class="status-val" id="loc-display">--</span></span>
<span>SCORE: <span class="status-val" id="score-display">0</span></span>
<span>DAY: <span class="status-val" id="day-display">1</span></span>
<span>CREW: <span class="status-val" id="crew-display">3/3</span></span>
</div>
</div>
<div id="output">Initializing the voyage...</div>
<div id="inventory-bar"></div>
<div class="backdrop" id="backdrop"></div>
<div id="side-panel">
<h3>&#128220; Voyage Log</h3>
<div id="score-detail"></div>
<h3>&#128373; Crew</h3>
<ul id="crew-list"></ul>
<button id="restart-btn">&#128260; New Voyage</button>
</div>
<div id="input-row">
<span id="prompt">&#9656;</span>
<input type="text" id="cmd" autofocus placeholder="Type a command...">
<button id="send">Go</button>
</div>
</div>
<div id="side-toggle" title="Voyage Log">&#9776;</div>
<script>
const output=document.getElementById('output'),cmd=document.getElementById('cmd'),sendBtn=document.getElementById('send')
const locD=document.getElementById('loc-display'),scoreD=document.getElementById('score-display'),dayD=document.getElementById('day-display'),crewD=document.getElementById('crew-display')
const invBar=document.getElementById('inventory-bar'),crewList=document.getElementById('crew-list'),scoreDetail=document.getElementById('score-detail')
const sideToggle=document.getElementById('side-toggle'),sidePanel=document.getElementById('side-panel'),backdrop=document.getElementById('backdrop'),restartBtn=document.getElementById('restart-btn')
let gameOver=false,cmdHistory=[],histIdx=-1

function scrollBtm(){setTimeout(()=>output.scrollTop=output.scrollHeight,30)}
function addMsg(text,cls=''){
  const div=document.createElement('div');div.className='msg'+(cls?' '+cls:'')
  // Detect content type for styling
  const t=text||''
  if(t.startsWith('> '))div.classList.add('sys')
  else if(t.startsWith('==='))div.classList.add('loc')
  else if(t.includes('OINK')||t.includes('HA HA')||t.includes('joke'))div.classList.add('humor')
  else if(t.includes('strike')||t.includes('sword')||t.includes('fight'))div.classList.add('combat')
  div.textContent=t;output.appendChild(div);scrollBtm()
}
function updateUI(d){
  locD.textContent=(d.location||'?').replace(/_/g,' ').replace(/\b\w/g,c=>c.toUpperCase())
  scoreD.textContent=d.score??0;dayD.textContent=d.days??1
  crewD.textContent=(d.crew_alive||'?')+'/'+(d.crew_total||'?')
  // Inventory bar
  invBar.innerHTML=''
  if(d.inventory&&d.inventory.length){
    d.inventory.forEach(i=>{const s=document.createElement('span');s.className='inv-item';s.textContent=i;invBar.appendChild(s)})
  }
  // Side panel
  crewList.innerHTML=''
  if(d.crew){
    d.crew.forEach(c=>{const li=document.createElement('li');li.textContent=c.name+' ('+c.role+')';if(!c.alive)li.classList.add('dead');crewList.appendChild(li)})
  }
  scoreDetail.innerHTML='Islands: <span>'+d.islands_visited+'</span> | Items: <span>'+(d.inventory?.length||0)+'</span>'
  gameOver=d.game_over||false;cmd.disabled=gameOver;sendBtn.disabled=gameOver;cmd.placeholder=gameOver?'The voyage has ended. New Voyage to sail again.':'Type a command...'
}
async function sendCmd(){
  const text=cmd.value.trim();if(!text||gameOver)return
  cmdHistory.push(text);histIdx=cmdHistory.length;cmd.value=''
  addMsg('> '+text)
  try{
    const r=await fetch('/api/command',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({command:text})})
    const d=await r.json()
    if(d.restart){output.innerHTML='';addMsg('A new voyage begins...')}
    addMsg(d.output||'')
    updateUI(d)
    if(d.game_over){addMsg('\n\u2500\u2500\u2500 The End \u2500\u2500\u2500\nThank you for sailing with Mael Duin.','loc')}
  }catch(e){addMsg('\u26a0 Connection lost: '+e.message,'err')}
}
cmd.addEventListener('keydown',e=>{
  if(e.key==='Enter')sendCmd()
  if(e.key==='ArrowUp'){e.preventDefault();if(histIdx>0){histIdx--;cmd.value=cmdHistory[histIdx]||''}}
  if(e.key==='ArrowDown'){e.preventDefault();if(histIdx<cmdHistory.length-1){histIdx++;cmd.value=cmdHistory[histIdx]||''}else{histIdx=cmdHistory.length;cmd.value=''}}
})
sendBtn.addEventListener('click',sendCmd)
sideToggle.addEventListener('click',()=>{sidePanel.classList.toggle('open');backdrop.classList.toggle('show')})
backdrop.addEventListener('click',()=>{sidePanel.classList.remove('open');backdrop.classList.remove('show')})
restartBtn.addEventListener('click',async()=>{
  if(!confirm('Set sail on a new voyage? All progress will be lost.'))return
  output.innerHTML='';gameOver=false;cmd.disabled=false;sendBtn.disabled=false;cmd.placeholder='Type a command...'
  try{
    const r=await fetch('/api/start',{method:'POST'});const d=await r.json()
    addMsg(d.output||'Your voyage begins...');updateUI(d);cmd.focus()
  }catch(e){addMsg('\u26a0 Error: '+e.message,'err')}
})
// Auto-start
(async()=>{
  try{const r=await fetch('/api/start',{method:'POST'});const d=await r.json();addMsg(d.output||'');updateUI(d);cmd.focus()}
  catch(e){addMsg('\u26a0 Could not start game. Is the server running?','err')}
})()
</script>
</body>
</html>"""

class GameHandler(BaseHTTPRequestHandler):
    def _json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length",str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)
    def _html(self, html, status=200):
        body = html.encode()
        self.send_response(status)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Content-Length",str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
    def _sid(self):
        c = self.headers.get("Cookie","")
        for s in c.split(";"):
            s=s.strip()
            if s.startswith("session="): return s[8:]
        return None
    def _state_json(self, state, output=""):
        return {
            "output": output, "location": state.current_location,
            "inventory": [i.name for i in state.inventory],
            "score": state.score, "turns": state.turns, "days": state.days,
            "game_over": state.game_over, "won": state.won,
            "crew_alive": state.total_crew_alive(), "crew_total": len(state.crew),
            "islands_visited": sum(1 for k in state.flags if k.endswith("_visited")),
            "crew": [{"name":c.name,"role":c.role,"alive":c.alive} for c in state.crew],
        }
    def do_OPTIONS(self):
        self.send_response(200); self._cors(); self.end_headers()
    def do_GET(self):
        p = urlparse(self.path).path
        if p=="/" or p=="/index.html": self._html(HTML)
        else:
            sp = os.path.join(os.path.dirname(__file__),"static",p.lstrip("/"))
            if os.path.isfile(sp):
                ct,_ = mimetypes.guess_type(sp) or ("application/octet-stream",)
                with open(sp,"rb") as f: b=f.read()
                self.send_response(200)
                self.send_header("Content-Type",ct)
                self.send_header("Content-Length",str(len(b)))
                self._cors(); self.end_headers(); self.wfile.write(b)
            else: self._json({"error":"Not found"},404)
    def do_POST(self):
        p = urlparse(self.path).path
        sid = self._sid()
        if p=="/api/start":
            sid = sid or str(uuid.uuid4())
            game_states[sid] = GameState()
            state = game_states[sid]
            out = handle_look(state, [])
            self.send_response(200); self._cors()
            self.send_header("Set-Cookie",f"session={sid};Path=/;HttpOnly;SameSite=Lax")
            self.send_header("Content-Type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(self._state_json(state, out)).encode())
            return
        elif p=="/api/command":
            state = game_states.get(sid) if sid else None
            if not state: self._json({"error":"No game session."},400); return
            cl = int(self.headers.get("Content-Length",0))
            body = self.rfile.read(cl) if cl else b"{}"
            data = json.loads(body)
            cmd = data.get("command","").strip()
            if not cmd: self._json({"error":"Empty command."},400); return
            result = process_command(state, cmd)
            if result == "__RESTART__":
                game_states[sid] = GameState()
                state = game_states[sid]
                out = handle_look(state, [])
                d = self._state_json(state, out); d["restart"]=True
                self._json(d); return
            self._json(self._state_json(state, result))
            return
        self._json({"error":"Not found"},404)

def main():
    port = int(os.environ.get("PORT", 5000))
    server = HTTPServer(("0.0.0.0", port), GameHandler)
    print(f"\n  \uD83C\uDF0A The Voyage of Mael Duin \u2014 Web Edition")
    print(f"  \uD83D\uDCD6  http://localhost:{port}")
    print(f"  \u2693  Press Ctrl+C to stop\n")
    try: server.serve_forever()
    except KeyboardInterrupt: print("\nFarewell, voyager!"); server.server_close()

if __name__ == "__main__": main()
