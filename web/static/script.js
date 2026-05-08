/* The Voyage of Mael Duin - Frontend Script */

(function() {
    'use strict';

    const outputContent = document.getElementById('output-content');
    const outputArea = document.getElementById('output-area');
    const commandInput = document.getElementById('command-input');
    const sendBtn = document.getElementById('send-btn');
    const inventoryList = document.getElementById('inventory-list');
    const locDisplay = document.getElementById('loc-display');
    const scoreDisplay = document.getElementById('score-display');
    const turnDisplay = document.getElementById('turn-display');
    const restartBtn = document.getElementById('restart-btn');
    const panelToggle = document.getElementById('panel-toggle');
    const sidePanel = document.getElementById('side-panel');

    let gameOver = false;

    // ---- Utility ----

    function scrollToBottom() {
        setTimeout(() => {
            outputArea.scrollTop = outputArea.scrollHeight;
        }, 50);
    }

    function appendOutput(text, className = '') {
        const block = document.createElement('div');
        block.className = 'output-block' + (className ? ' ' + className : '');
        block.textContent = text;
        outputContent.appendChild(block);
        scrollToBottom();
        return block;
    }

    function clearOutput() {
        outputContent.innerHTML = '';
    }

    function updateUI(state) {
        if (state.location) {
            locDisplay.textContent = 'Location: ' + state.location.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        }
        if (state.score !== undefined) {
            scoreDisplay.textContent = 'Score: ' + state.score;
        }
        if (state.turns !== undefined) {
            turnDisplay.textContent = 'Turn: ' + state.turns;
        }

        // Update inventory
        inventoryList.innerHTML = '';
        if (state.inventory && state.inventory.length > 0) {
            state.inventory.forEach(item => {
                const li = document.createElement('li');
                li.textContent = '▸ ' + item;
                inventoryList.appendChild(li);
            });
        } else {
            inventoryList.innerHTML = '<li style="color:#555;">Empty</li>';
        }

        gameOver = state.game_over || false;
    }

    // ---- API Calls ----

    async function sendCommand(cmd) {
        try {
            const resp = await fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd }),
            });
            const data = await resp.json();

            if (data.error) {
                appendOutput(data.error, 'error-msg');
                return;
            }

            if (data.restart) {
                clearOutput();
            }

            appendOutput('> ' + cmd, 'system-msg');

            // Split output by location headers for nice formatting
            const output = data.output || '';
            const lines = output.split('\n');
            let formatted = '';
            lines.forEach(line => {
                if (line.startsWith('=== ') && line.endsWith(' ===')) {
                    formatted += '\n' + line + '\n';
                } else {
                    formatted += line + '\n';
                }
            });

            appendOutput(formatted.trim());

            updateUI(data);

            if (data.game_over) {
                appendOutput('\n--- The End ---\nThank you for playing The Voyage of Mael Duin!', 'system-msg');
                commandInput.disabled = true;
                sendBtn.disabled = true;
                commandInput.placeholder = 'Game over. Start a new voyage.';
            }

            return data;
        } catch (err) {
            appendOutput('⚠ Connection error: ' + err.message, 'error-msg');
        }
    }

    async function startGame() {
        try {
            const resp = await fetch('/api/start', { method: 'POST' });
            const data = await resp.json();
            clearOutput();
            appendOutput(data.output || 'Your voyage begins...');
            updateUI(data);
            commandInput.disabled = false;
            sendBtn.disabled = false;
            commandInput.focus();
        } catch (err) {
            appendOutput('⚠ Could not start game: ' + err.message, 'error-msg');
        }
    }

    // ---- Event Handlers ----

    function handleSubmit() {
        const cmd = commandInput.value.trim();
        if (!cmd || gameOver) return;

        commandInput.value = '';
        sendCommand(cmd);
    }

    commandInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleSubmit();
        }
    });

    sendBtn.addEventListener('click', handleSubmit);

    restartBtn.addEventListener('click', function() {
        if (confirm('Start a new voyage? All progress will be lost.')) {
            gameOver = false;
            commandInput.disabled = false;
            sendBtn.disabled = false;
            commandInput.placeholder = 'Type a command...';
            startGame();
        }
    });

    panelToggle.addEventListener('click', function() {
        sidePanel.classList.toggle('open');
    });

    // Close side panel on click outside
    document.addEventListener('click', function(e) {
        if (sidePanel.classList.contains('open') &&
            !sidePanel.contains(e.target) &&
            e.target !== panelToggle) {
            sidePanel.classList.remove('open');
        }
    });

    // ---- Init ----

    startGame();
})();
