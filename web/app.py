#!/usr/bin/env python3
"""The Voyage of Mael Duin - Web Edition (Flask)"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from flask import Flask, render_template, request, jsonify, session
from game.engine import GameState, process_command, handle_look

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

# Store game states in memory (simple approach)
game_states = {}


def get_or_create_state(sid):
    if sid not in game_states:
        state = GameState()
        from game import world  # noqa: F401
        game_states[sid] = state
    return game_states[sid]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/start", methods=["POST"])
def start_game():
    sid = session.get("sid")
    if not sid:
        import uuid
        sid = str(uuid.uuid4())
        session["sid"] = sid

    state = get_or_create_state(sid)
    from game import world  # noqa: F401
    output = handle_look(state, [])

    return jsonify({
        "output": output,
        "location": state.current_location,
        "inventory": [i.name for i in state.inventory],
        "score": state.score,
        "turns": state.turns,
        "game_over": state.game_over,
    })


@app.route("/api/command", methods=["POST"])
def handle_command():
    sid = session.get("sid")
    if not sid:
        return jsonify({"error": "No game session. Start a new game first."}), 400

    state = game_states.get(sid)
    if not state:
        return jsonify({"error": "Game session not found. Start a new game."}), 400

    data = request.get_json()
    cmd = data.get("command", "").strip()

    if not cmd:
        return jsonify({"error": "Empty command."}), 400

    result = process_command(state, cmd)

    if result == "__RESTART__":
        state = GameState()
        from game import world  # noqa: F401
        game_states[sid] = state
        output = handle_look(state, [])
        return jsonify({
            "output": output,
            "restart": True,
            "location": state.current_location,
            "inventory": [],
            "score": 0,
            "turns": 0,
            "game_over": False,
        })

    return jsonify({
        "output": result,
        "location": state.current_location,
        "inventory": [i.name for i in state.inventory],
        "score": state.score,
        "turns": state.turns,
        "game_over": state.game_over,
    })


@app.route("/api/state", methods=["GET"])
def get_state():
    sid = session.get("sid")
    if not sid:
        return jsonify({"error": "No game session."}), 400

    state = game_states.get(sid)
    if not state:
        return jsonify({"error": "No game session."}), 400

    return jsonify({
        "location": state.current_location,
        "inventory": [i.name for i in state.inventory],
        "score": state.score,
        "turns": state.turns,
        "game_over": state.game_over,
        "flags": {k: v for k, v in state.flags.items() if k.endswith("_visited")},
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
