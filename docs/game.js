/* The Voyage of Mael Duin — JavaScript Game Engine
   Pure client-side port of the Python engine for GitHub Pages. */

// ─── DATA ──────────────────────────────────────────────────────────
let G = null;  // game_data loaded from JSON
let STATE = null;

function loadGameData(data) {
  G = data;
}

// ─── HELPERS ────────────────────────────────────────────────────────

function matchItem(text, items) {
  const t = text.toLowerCase().trim();
  for (const item of items) {
    if (t === item.id || t === item.name.toLowerCase()) return item;
    for (const a of (item.aliases || [])) {
      if (t === a.toLowerCase()) return item;
    }
  }
  return null;
}

function matchNpc(text, npcs) {
  const t = text.toLowerCase().trim();
  for (const npc of npcs) {
    if (t === npc.id || t === npc.name.toLowerCase()) return npc;
    for (const a of (npc.aliases || [])) {
      if (t === a.toLowerCase()) return npc;
    }
  }
  return null;
}

function getLocation(id) {
  return G.locations[id] || null;
}

function getNpc(id) {
  return G.npcs[id] || null;
}

function getItem(id) {
  return G.items[id] || null;
}

// ─── GAME STATE ─────────────────────────────────────────────────────

function newState() {
  return {
    location: 'home',
    inventory: [],
    flags: {},
    score: 0,
    turns: 0,
    days: 0,
    gameOver: false,
    won: false,
    crew: JSON.parse(JSON.stringify(G.crew)).map(c => ({...c, alive: true})),
    awaitingChoice: null,
    choiceData: null,
    visited: {},
  };
}

function hasFlag(flag) { return !!STATE.flags[flag]; }
function setFlag(flag, v) { STATE.flags[flag] = v === undefined ? true : v; }

function getLocItems() {
  const loc = getLocation(STATE.location);
  if (!loc) return [];
  return (loc.items || []).map(id => getItem(id)).filter(Boolean);
}

function getLocNpcs() {
  const loc = getLocation(STATE.location);
  if (!loc) return [];
  return (loc.npcs || []).map(id => getNpc(id)).filter(Boolean);
}

function getInvItem(text) {
  return matchItem(text, STATE.inventory);
}

function getLocItem(text) {
  return matchItem(text, getLocItems());
}

function findItem(text) {
  return getInvItem(text) || getLocItem(text);
}

function getNpcHere(text) {
  return matchNpc(text, getLocNpcs());
}

function totalCrewAlive() {
  return STATE.crew.filter(c => c.alive).length;
}

function loseCrew(id) {
  const alive = STATE.crew.filter(c => c.alive);
  const member = id ? alive.find(c => c.id === id) : alive[Math.floor(Math.random() * alive.length)];
  if (member) { member.alive = false; return member; }
  return null;
}

// ─── LOCATION HELPERS ────────────────────────────────────────────────

const DIR_MAP = {
  n:'north', north:'north', s:'south', south:'south',
  e:'east', east:'east', w:'west', west:'west',
  ne:'northeast', northeast:'northeast', nw:'northwest', northwest:'northwest',
  se:'southeast', southeast:'southeast', sw:'southwest', southwest:'southwest',
  u:'up', up:'up', d:'down', down:'down',
  deeper:'deeper', deep:'deeper', back:'back', return:'back', shallows:'shallows',
  home:'home', in:'in', inside:'in', enter:'in',
  cross:'cross', bridge:'cross', out:'out', exit:'out', leave:'out',
  through:'through', climb:'climb', gold:'gold',
};

function getExitsText() {
  const loc = getLocation(STATE.location);
  if (!loc) return '';
  const blocked = loc.blocked || {};
  const avail = Object.entries(loc.exits || {}).map(([d, _]) => {
    if (blocked[d]) return `${d} (${blocked[d]})`;
    return d;
  });
  return avail.length ? 'Exits: ' + avail.join(', ') : '';
}

// ─── HANDLERS ─────────────────────────────────────────────────────────

function h_unknown(cmd) {
  return `I don't understand "${cmd}". Type HELP for a list of commands.`;
}

function h_help() {
  return `=== THE VOYAGE OF MAEL DUIN ===

Commands:
  LOOK / L               - Describe your surroundings
  GO [dir] / [dir]       - Move (north/south/east/west/sea)
  TAKE [item]            - Pick up an item
  DROP [item]            - Drop an item
  INVENTORY / I          - Check what you're carrying
  EXAMINE / X [item]     - Look closely at something
  TALK TO [npc]          - Speak with someone
  GIVE [item] TO [npc]   - Offer something
  USE [item] [with item] - Use an item
  SAIL                   - Set sail on the open sea
  FIGHT [target]         - Engage in combat
  JOKE TO [npc]          - Tell someone a joke
  SING [song]            - Belt out a tune
  YES / NO               - Respond to a choice
  WAIT / Z               - Pass time
  CREW                   - Check on your crew
  SCORE                  - See your progress
  QUIT / Q               - End the voyage
  RESTART                - Start over
  HELP                   - Show this message

Tip: Try EXAMINE things and TALK TO people!`;
}

function h_look() {
  const loc = getLocation(STATE.location);
  if (!loc) return 'The void stares back. You are nowhere.';

  const firstVisit = !STATE.visited[loc.id];
  STATE.visited[loc.id] = true;

  let text = `\n=== ${loc.name} ===\n\n`;
  text += firstVisit ? loc.detailed_desc + '\n' : loc.description + '\n';

  const items = getLocItems();
  if (items.length) {
    text += `\nYou see: ${items.map(i => i.name).join(', ')}\n`;
  }

  const npcs = getLocNpcs();
  for (const n of npcs) {
    text += `\n${n.name} is here.\n`;
  }

  text += '\n' + getExitsText();

  // Homecoming special
  if (loc.id === 'homecoming' && !hasFlag('confronted')) {
    setFlag('confronted');
    STATE.awaitingChoice = 'ending';
    text += '\n\nType YES to forgive them. Type NO to take your vengeance.';
  }

  return text;
}

function h_go(direction) {
  const dir = (DIR_MAP[direction.toLowerCase()] || direction).toLowerCase();
  const loc = getLocation(STATE.location);
  if (!loc) return 'You are lost.';

  const blocked = loc.blocked || {};
  if (blocked[dir]) return blocked[dir];

  const exits = loc.exits || {};
  if (!exits[dir]) return `You cannot go ${dir} from here.`;

  const newLocId = exits[dir];
  const newLoc = getLocation(newLocId);
  if (!newLoc) return `You try to go ${dir} but find nothing there.`;

  STATE.location = newLocId;
  STATE.turns++;

  let result = '';

  // Special on_enter events (hardcoded for key locations)
  if (newLocId === 'ants_grove' && !hasFlag('ants_pacified')) {
    result += `The queen ant clicks her mandibles three times. A single ant approaches you, holding a golden fruit in its jaws. It offers it to you.\n\nIt seems the ants are... friendly? Or they think you're a very ugly ant.\n\n`;
  }
  if (newLocId === 'hermit_rock' && !hasFlag('met_hermit')) {
    setFlag('met_hermit');
    result += `The hermit's blessing washes over you as you step onto the rock. For a moment, the weight of your quest lifts from your shoulders.\n\n`;
  }
  if (newLocId === 'sea_monsters' && !hasFlag('sea_monster_defeated')) {
    result += `A monstrous hand erupts from the water, clutching the gunwale of your curragh! The boat lurches violently. Crew members grab for their swords.\n\nYou have a moment to act! FIGHT it with your sword, or use an item!\n\n`;
  }
  if (newLocId === 'homecoming' && !hasFlag('confronted')) {
    result += `The wind carries the smell of home. Your crew stands behind you, weapons drawn.\n\nThis is the moment your voyage was meant to end. But how?\n\n`;
  }

  result += h_look();
  return result;
}

function h_take(itemName) {
  if (!itemName) return 'Take what?';
  const loc = getLocation(STATE.location);
  if (!loc) return "There's nothing here.";

  const item = getLocItem(itemName);
  if (!item) return `You don't see any "${itemName}" here.`;
  if (!item.takeable) return `You can't take the ${item.name}. ${item.description}`;
  if (STATE.inventory.length >= 10) return 'Your hands are full. Drop something first.';

  STATE.inventory.push(item);
  return `You take the ${item.name}.`;
}

function h_drop(itemName) {
  if (!itemName) return 'Drop what?';
  const item = getInvItem(itemName);
  if (!item) return `You don't have "${itemName}".`;
  STATE.inventory = STATE.inventory.filter(i => i.id !== item.id);
  return `You drop the ${item.name}.`;
}

function h_inventory() {
  if (!STATE.inventory.length) return 'You are carrying nothing.';
  return 'You are carrying:\n' + STATE.inventory.map(i => `  - ${i.name}: ${i.description}`).join('\n');
}

function h_examine(target) {
  if (!target) return 'Examine what?';

  let item = getInvItem(target);
  if (item) return item.examine;

  item = getLocItem(target);
  if (item) return item.examine;

  const npc = getNpcHere(target);
  if (npc) return npc.description;

  return `You see nothing special about "${target}".`;
}

function h_talk(npcName) {
  if (!npcName) return 'Talk to whom?';
  const npc = getNpcHere(npcName);
  if (!npc) return `There's no one named "${npcName}" here to talk to.`;

  const dialog = npc.dialogue || {};
  if (dialog.greeting) {
    let result = dialog.greeting;

    // Queen special
    if (npc.id === 'queen' && !hasFlag('queen_choice_offered')) {
      setFlag('queen_choice_offered');
      STATE.awaitingChoice = 'queen_stay';
      result += '\n\n(Type YES to stay. Type NO to resist and leave.)';
    }

    return result;
  }
  return `${npc.name} looks at you but says nothing.`;
}

function h_give(text) {
  const parts = text.split(/\s+to\s+/);
  if (parts.length < 2) return 'Give what to whom? Usage: GIVE [item] TO [npc]';

  const itemName = parts[0].trim();
  const npcName = parts[1].trim();

  const item = getInvItem(itemName);
  if (!item) return `You don't have "${itemName}".`;

  const npc = getNpcHere(npcName);
  if (!npc) return `There's no "${npcName}" here.`;

  // Cat takes milk
  if (npc.id === 'cat' && item.id === 'talking_cat_tribute') {
    STATE.inventory = STATE.inventory.filter(i => i.id !== item.id);
    setFlag('cat_pacified');
    STATE.score++;
    const pearl = getItem('pearl');
    if (pearl) STATE.inventory.push(pearl);
    return `You offer the bowl of milk to the cat. It sniffs once, then delicately laps it all up.

"Acceptable tribute. You may pass through my island safely. And take this — a cat always pays its debts."

The cat produces a shimmering Pearl from somewhere (you're not sure where) and drops it at your feet.

(+1 point, and you've earned the cat's respect.)`;
  }

  return `You offer the ${item.name} to ${npc.name}. They look at you strangely and don't take it.`;
}

function h_use(text) {
  if (!text || !text.trim()) return 'Use what? Usage: USE [item] [with target]';
  const parts = text.split(/\s+(?:with|on|at|in)\s+/);
  const itemName = parts[0].trim();
  const targetName = parts.length > 1 ? parts[1].trim() : null;

  const item = getInvItem(itemName) || getLocItem(itemName);
  if (!item) return `You don't have "${itemName}".`;

  if (item.use_text) return item.use_text;
  return `You use the ${item.name}. Nothing happens.`;
}

function h_wait() {
  STATE.turns++;
  return 'Time passes...';
}

function h_crew() {
  const alive = STATE.crew.filter(c => c.alive);
  const dead = STATE.crew.filter(c => !c.alive);
  let text = '=== YOUR CREW ===\n';
  for (const c of alive) text += `  ${c.name} (${c.role}) - ${c.description}\n`;
  if (dead.length) {
    text += '\n--- Lost ---\n';
    for (const c of dead) text += `  ${c.name} - ${c.role}\n`;
  }
  text += `\n${alive.length} alive, ${dead.length} lost`;
  return text;
}

function h_score() {
  const visited = Object.keys(STATE.visited).length;
  return `=== SCORE ===
Turns: ${STATE.turns}
Score: ${STATE.score}
Islands visited: ${visited}
Items carried: ${STATE.inventory.length}
Crew alive: ${totalCrewAlive()}/${STATE.crew.length}
Game over: ${STATE.gameOver}`;
}

function h_quit() {
  STATE.gameOver = true;
  return 'Your voyage ends here. Farewell, Mael Duin.';
}

function h_restart() {
  return '__RESTART__';
}

function h_sail() {
  const loc = getLocation(STATE.location);
  if (!loc) return 'You are on land.';
  if (loc.id === 'home') return 'You are on land. You need to be at sea or on the shore to sail.';

  // Try to find any exit that leads back to sea
  for (const [direction, target] of Object.entries(loc.exits || {})) {
    if (target.startsWith('sea')) return h_go(direction);
  }

  return "There's nowhere to sail from here. Try a direction (north/south/east/west) to find the sea.";
}

function h_fight(target) {
  if (!target) return 'Fight what? Use: FIGHT [target]';

  const locId = STATE.location;

  if (locId === 'sea_monsters' && !hasFlag('sea_monster_defeated')) {
    // Has harpoon?
    if (getInvItem('harpoon') || getInvItem('magic_harpoon')) {
      setFlag('sea_monster_defeated');
      STATE.score += 5;
      return `You hurl the magic harpoon at the monstrous hand! It strikes true, and with a roar that shakes the sea, the creature releases the boat and sinks back into the depths. The water is still once more.

Your crew cheers. Conganchnes claps you on the back. 'Good throw, Captain!'`;
    }
    // Conganchnes alive?
    const congan = STATE.crew.find(c => c.id === 'conganchnes');
    if (congan && congan.alive) {
      setFlag('sea_monster_defeated');
      STATE.score += 3;
      return `Conganchnes leaps onto the monster's hand, his legendary skin turning aside its claws! He drives his sword deep into the creature's wrist, and with a howl of pain, it releases the boat and sinks beneath the waves.

Conganchnes lands back on deck, dripping with ichor. 'Next time, you fight the sea monster.'`;
    }
    return `You draw your sword and strike at the monstrous hand! The blade bounces off its leathery skin. It barely seems to notice. You need a better weapon, or a stronger warrior.`;
  }

  if (locId === 'black_pig' && !hasFlag('apple_taken')) {
    return `The black pig snorts and charges! Its tusks are the size of daggers. Before you can react, it bowls you over and stands triumphantly on your chest.

"OINK," it says, with evident satisfaction. It then wanders back to the tree and goes to sleep.

You are unharmed, but your pride is in tatters. You were defeated by a pig.`;
  }

  return `There's nothing to fight here. You can't just attack ${target} for no reason.`;
}

function h_joke(text) {
  if (!text) return 'Tell a joke to whom? Use: JOKE TO [npc]';

  const king = getNpcHere('king');
  if (!king) return "There's no one here who wants to hear a joke.";

  if (hasFlag('king_pacified')) {
    return 'The Laughing King wipes a tear from his eye. "You already told me the best one! I can\'t take another!"';
  }

  setFlag('king_pacified');
  STATE.score += 2;

  // Add laughing potion to location
  const loc = getLocation(STATE.location);
  const potion = getItem('laughing_potion');
  if (loc && potion && !(loc.items || []).includes('laughing_potion')) {
    if (!loc.items) loc.items = [];
    loc.items.push('laughing_potion');
  }

  return `You tell a joke: "${text}"

The Laughing King freezes. His eyes go wide. For a moment, there is silence.

Then he ERUPTS — laughing so hard he falls off his stool, rolls on the ground, and pounds the earth with his fists. His subjects are laughing too, but at him, not with him.

"THAT'S the one! THAT'S the BEST joke I've ever heard!" He gasps between gales of laughter. "Here, take this! It's the Laughing Potion — one sip and you'll be as happy as me!"

He tosses you a bubbling vial.

(+2 points. The island is now quiet — well, quieter.)`;
}

function h_sing(text) {
  if (!text) return 'Sing what? Use: SING [song]';
  if (STATE.location === 'sea1') {
    return `You belt out a shanty: "${text}"

Your crew joins in, their rough voices carrying across the waves. Diurán quickly scribbles down the lyrics, muttering about copyright.`;
  }
  return `You sing: "${text}"

Your voice cracks slightly on the high notes, but you give it your all. A nearby seal applauds by slapping its flippers together.`;
}

function h_yes() {
  if (STATE.awaitingChoice === 'queen_stay') {
    return _queenStay();
  }
  if (STATE.awaitingChoice === 'ending') {
    return _endingForgive();
  }
  return "Yes to what? There's no pending choice.";
}

function h_no() {
  if (STATE.awaitingChoice === 'queen_stay') {
    setFlag('resisted_queen');
    STATE.score += 5;
    STATE.awaitingChoice = null;
    return `"No," you say firmly. "We must continue our voyage."

The Queen's smile flickers. For a moment, you see something ancient and cold in her eyes. Then she laughs — a sound like breaking glass.

"As you wish, Mael Duin. But remember: not all who stay are prisoners, and not all who leave are free."

She waves her hand, and you find yourself back on your curragh, bobbing on the open sea. Days — or weeks? — have passed. Your crew looks older, wearier. They remember everything.

You have resisted the ultimate temptation.`;
  }
  if (STATE.awaitingChoice === 'ending') {
    return _endingVengeance();
  }
  return "No to what? There's no pending choice.";
}

function _queenStay() {
  setFlag('stayed_with_queen');
  STATE.days += 30;
  STATE.score += 1;
  const lost = loseCrew();
  STATE.awaitingChoice = null;
  return `You stay. Days turn to weeks. Weeks to months.

The feasts are glorious. The wine flows like rivers. The Queen's laughter is music, and her touch is fire. Your crew forgets the voyage. You almost forget your father.

But one morning, you wake to find one of your crew has vanished. Then another. The beautiful women grow pale and thin. The food tastes like ash.

You gather what remains of your crew and flee to the curragh. As you push off from shore, the Queen watches from the palace steps, smiling her cold smile.

Months have passed in the real world. Your crew is smaller. Your quest feels more urgent than ever.

(You lost ${lost ? lost.name : 'a crew member'} to the Queen's enchantment. 30 days have passed.)`;
}

function _endingForgive() {
  STATE.awaitingChoice = null;
  STATE.gameOver = true;
  STATE.won = true;
  const islands = Object.keys(STATE.visited).length;
  STATE.score += islands * 2;
  return `You lower your sword.

"Go," you say. "I did not sail across the edge of the world, visit thirty islands, fight giant ants and talking cats and laughing kings, to become the same kind of man who killed my father."

The raiders stare at you. The eldest — grey-bearded, one-eyed — nods slowly.

"Your father was a good man," he says. "He died well. I have carried his death like a stone in my chest ever since. Thank you, Mael Duin, for lifting it."

They leave their weapons on the sand and walk away into the mist.

Your crew gathers around you. Diurán is weeping. Conganchnes sheathes his sword. Fergus puts a hand on your shoulder.

"Well," says the poet, "that's a better ending than I'd written."

You return to your village a different man. The druid is waiting for you by the fire. He smiles — the first time you've ever seen him smile.

"I see the sea has taught you what I could not," he says.

=== THE END ===
Thank you for playing The Voyage of Mael Duin.
Final score: ${STATE.score} | Islands visited: ${islands} | Days at sea: ${STATE.days} | Crew survived: ${totalCrewAlive()}/${STATE.crew.length}

"Forgiveness is a cup that fills the drinker."`;
}

function _endingVengeance() {
  STATE.awaitingChoice = null;
  STATE.gameOver = true;
  STATE.won = true;
  const islands = Object.keys(STATE.visited).length;
  STATE.score += islands;
  return `You raise your sword.

"For my father!" you cry, and your crew charges with you.

The battle is short and brutal. Conganchnes cuts through three men before they can draw breath. The grey-bearded raider falls to his knees before you, and you drive your blade home.

It is done. Your father is avenged.

But as you stand over the body, you feel... empty. The prophecy scroll hangs heavy in your pack. Diurán has stopped writing. He has nothing to say.

You return to your village a victor. The druid is waiting. He looks at you with sad eyes.

"You have your revenge, Mael Duin. I hope it keeps you warm at night."

It doesn't.

=== THE END ===
Thank you for playing The Voyage of Mael Duin.
Final score: ${STATE.score} | Islands visited: ${islands} | Days at sea: ${STATE.days} | Crew survived: ${totalCrewAlive()}/${STATE.crew.length}

"Vengeance is a cup that empties the drinker."`;
}

// ─── PARSER ────────────────────────────────────────────────────────────

const VERBS = {
  look: h_look, l: h_look,
  go: h_go, north: (_,a)=>h_go('north'), n: (_,a)=>h_go('north'),
  south: (_,a)=>h_go('south'), s: (_,a)=>h_go('south'),
  east: (_,a)=>h_go('east'), e: (_,a)=>h_go('east'),
  west: (_,a)=>h_go('west'), w: (_,a)=>h_go('west'),
  northeast: (_,a)=>h_go('northeast'), ne: (_,a)=>h_go('northeast'),
  northwest: (_,a)=>h_go('northwest'), nw: (_,a)=>h_go('northwest'),
  southeast: (_,a)=>h_go('southeast'), se: (_,a)=>h_go('southeast'),
  southwest: (_,a)=>h_go('southwest'), sw: (_,a)=>h_go('southwest'),
  up: (_,a)=>h_go('up'), u: (_,a)=>h_go('up'),
  down: (_,a)=>h_go('down'), d: (_,a)=>h_go('down'),
  take: h_take, get: h_take,
  drop: h_drop, discard: h_drop,
  inventory: h_inventory, i: h_inventory,
  examine: h_examine, x: h_examine,
  talk: h_talk, speak: h_talk,
  give: h_give, use: h_use,
  wait: h_wait, z: h_wait,
  crew: h_crew, score: h_score,
  quit: h_quit, q: h_quit, restart: h_restart,
  sail: h_sail,
  fight: h_fight, attack: h_fight,
  joke: h_joke, sing: h_sing,
  yes: h_yes, y: h_yes,
  no: h_no, nope: h_no,
  help: h_help, '?': h_help, h: h_help,
};

function parseCommand(text) {
  text = text.trim().replace(/\s+/g, ' ');
  if (!text) return [null, ''];

  const lower = text.toLowerCase();
  const words = lower.split(' ');

  // Multi-word patterns
  const patterns = [
    [/^look at\s+(.+)$/, h_examine], [/^look\s+(.+)$/, h_examine], [/^l\s+(.+)$/, h_examine],
    [/^examine\s+(.+)$/, h_examine], [/^x\s+(.+)$/, h_examine],
    [/^talk to\s+(.+)$/, h_talk], [/^talk with\s+(.+)$/, h_talk],
    [/^speak to\s+(.+)$/, h_talk], [/^speak with\s+(.+)$/, h_talk],
    [/^give\s+(.+)$/, h_give],
    [/^use\s+(.+)$/, h_use],
    [/^take\s+(.+)$/, h_take], [/^get\s+(.+)$/, h_take], [/^pick up\s+(.+)$/, h_take],
    [/^drop\s+(.+)$/, h_drop], [/^discard\s+(.+)$/, h_drop],
    [/^joke to\s+(.+)$/, h_joke], [/^joke\s+(.+)$/, h_joke],
    [/^fight\s+(.+)$/, h_fight], [/^attack\s+(.+)$/, h_fight],
    [/^sing\s+(.+)$/, h_sing],
  ];

  for (const [regex, handler] of patterns) {
    const m = lower.match(regex);
    if (m) return [handler, m[1].trim()];
  }

  // Bare "talk to" etc
  if (['talk to', 'speak to', 'talk with', 'speak with'].includes(lower)) {
    return [() => 'Talk to whom?', ''];
  }

  // Single word verb
  const first = words[0];
  const handler = VERBS[first];
  if (handler) return [handler, words.slice(1).join(' ')];

  // Direction aliases
  const dirAliases = {
    n:'north', s:'south', e:'east', w:'west',
    ne:'northeast', nw:'northwest', se:'southeast', sw:'southwest',
    u:'up', d:'down',
    deeper:'deeper', deep:'deeper', back:'back', return:'back', shallows:'shallows',
    home:'home', in:'in', inside:'in', enter:'in',
    cross:'cross', bridge:'cross', out:'out', exit:'out', leave:'out',
    through:'through', climb:'climb', gold:'gold',
  };
  if (dirAliases[first]) return [(_,a) => h_go(dirAliases[first]), ''];

  return [null, text];
}

function processCommand(text) {
  if (!text || !text.trim()) return "Type HELP for a list of commands, or just start exploring!";
  const [handler, args] = parseCommand(text);
  if (!handler) return h_unknown(text);
  return handler(STATE, args);
}

// ─── UI ────────────────────────────────────────────────────────────────

let cmdHistory = [];
let histIdx = 0;

function initUI() {
  const output = document.getElementById('output');
  const cmd = document.getElementById('cmd');
  const sendBtn = document.getElementById('send');
  const invBar = document.getElementById('inventory-bar');
  const locD = document.getElementById('loc-display');
  const scoreD = document.getElementById('score-display');
  const dayD = document.getElementById('day-display');
  const crewD = document.getElementById('crew-display');
  const crewList = document.getElementById('crew-list');
  const scoreDetail = document.getElementById('score-detail');
  const restartBtn = document.getElementById('restart-btn');

  function scrollBtm() { setTimeout(() => output.scrollTop = output.scrollHeight, 30); }

  function addMsg(text, cls) {
    const div = document.createElement('div');
    div.className = 'msg' + (cls ? ' ' + cls : '');
    div.textContent = text;
    output.appendChild(div);
    scrollBtm();
  }

  function updateUI() {
    const loc = getLocation(STATE.location);
    locD.textContent = loc ? loc.name : '—';
    scoreD.textContent = STATE.score;
    dayD.textContent = STATE.days + 1;
    crewD.textContent = totalCrewAlive() + '/' + STATE.crew.length;

    // Inventory bar
    invBar.innerHTML = '';
    for (const item of STATE.inventory) {
      const s = document.createElement('span');
      s.className = 'inv-item';
      s.textContent = item.name;
      invBar.appendChild(s);
    }

    // Crew list
    crewList.innerHTML = '';
    for (const c of STATE.crew) {
      const li = document.createElement('li');
      li.textContent = c.name + ' (' + c.role + ')';
      if (!c.alive) li.classList.add('dead');
      crewList.appendChild(li);
    }

    // Score details
    const visited = Object.keys(STATE.visited).length;
    scoreDetail.innerHTML = 'Islands: <span>' + visited + '</span> | Items: <span>' + STATE.inventory.length + '</span>';

    cmd.disabled = STATE.gameOver;
    sendBtn.disabled = STATE.gameOver;
    cmd.placeholder = STATE.gameOver ? 'The voyage has ended. New Voyage to sail again.' : 'Type a command...';
  }

  function sendCmd() {
    const text = cmd.value.trim();
    if (!text || STATE.gameOver) return;

    cmdHistory.push(text);
    histIdx = cmdHistory.length;
    cmd.value = '';

    addMsg('> ' + text, 'sys');

    let result;
    try {
      result = processCommand(text);
    } catch (e) {
      addMsg('⚠ Error: ' + e.message, 'err');
      console.error('Game error:', e);
      return;
    }

    if (result === '__RESTART__') {
      output.innerHTML = '';
      STATE = newState();
      addMsg(h_look());
      updateUI();
      cmd.focus();
      return;
    }

    addMsg(result);

    updateUI();

    if (STATE.gameOver) {
      addMsg('\n─── The End ───\nThank you for sailing with Mael Duin.', 'loc');
    }
  }

  cmd.addEventListener('keydown', e => {
    if (e.key === 'Enter') sendCmd();
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (histIdx > 0) { histIdx--; cmd.value = cmdHistory[histIdx] || ''; }
    }
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (histIdx < cmdHistory.length - 1) { histIdx++; cmd.value = cmdHistory[histIdx] || ''; }
      else { histIdx = cmdHistory.length; cmd.value = ''; }
    }
  });

  sendBtn.addEventListener('click', sendCmd);

  // Side panel toggle
  document.getElementById('side-toggle').addEventListener('click', () => {
    document.getElementById('side-panel').classList.toggle('open');
    document.getElementById('backdrop').classList.toggle('show');
  });
  document.getElementById('backdrop').addEventListener('click', () => {
    document.getElementById('side-panel').classList.remove('open');
    document.getElementById('backdrop').classList.remove('show');
  });

  restartBtn.addEventListener('click', () => {
    if (!confirm('Set sail on a new voyage? All progress will be lost.')) return;
    output.innerHTML = '';
    STATE = newState();
    addMsg(h_look());
    updateUI();
    cmd.focus();
  });

  return { addMsg, updateUI, sendCmd };
}

// ─── BOOT ───────────────────────────────────────────────────────────────

async function boot() {
  try {
    const resp = await fetch('game_data.json');
    const data = await resp.json();
    loadGameData(data);
    STATE = newState();
    const ui = initUI();
    ui.addMsg(h_look());
    ui.updateUI();
    document.getElementById('cmd').focus();
  } catch (e) {
    document.getElementById('output').textContent = '⚠ Error loading game data: ' + e.message;
  }
}

document.addEventListener('DOMContentLoaded', boot);
