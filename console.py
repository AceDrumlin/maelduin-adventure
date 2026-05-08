#!/usr/bin/env python3
"""The Voyage of Mael Duin - Console Edition"""

import sys
import os

# Use the system Python if running from venv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.engine import GameState, process_command, handle_look

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_slow(text, speed=0.0):
    """Print text with optional typewriter effect."""
    if speed > 0:
        import time
        for char in text:
            print(char, end="", flush=True)
            time.sleep(speed)
        print()
    else:
        print(text)

def main():
    clear_screen()

    title = r"""
  _______ _   _  ___    _   ___   __
 |__   __| | | || _ \  / | /_\ \ / /
    | |  | |_| ||  _/  | |/ _ \ V /
    |_|   \___/ |_|    |_/_/ \_\_/

    The Voyage of Mael Duin
    ========================
    A Classic Text Adventure
    """
    print(title)
    print("Type HELP for commands, or just start exploring!")
    print()

    state = GameState()

    # Import world data to populate locations
    from game import world  # noqa: F401

    print(handle_look(state, []))

    while not state.game_over:
        try:
            cmd = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nYour voyage ends here. Farewell, Mael Duin.")
            break

        if not cmd:
            continue

        result = process_command(state, cmd)

        if result == "__RESTART__":
            clear_screen()
            state = GameState()
            from game import world  # noqa: F401
            print(title)
            print(handle_look(state, []))
            continue

        print("\n" + result)

        if state.game_over:
            print("\n=== THE END ===")
            print(f"Final score: {state.score}")
            print("Thank you for playing The Voyage of Mael Duin!")
            break


if __name__ == "__main__":
    main()
