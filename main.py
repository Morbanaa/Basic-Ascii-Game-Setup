# Teddy Rodd
# Morbanaa Studios
# Basic Ascii Game Setup

import time
import keyboard
import os
import platform
from game_manager import Game_Manager

def main():
    game_speed = .05 # Smaller number = faster game speed
    game_manager = Game_Manager(80,25) # Pass in Width Height
    game_manager.world_gen()
    while True:
        # Update
        if keyboard.is_pressed("Q"):
            clear_screen()
            break

        # Render
        game_manager.render_game()

        # Util
        time.sleep(game_speed) # Game Clock
        game_manager.clear_move_cursor() # Moves cursor to top of console

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()

    # Last message
    print("Thanks for playing!\n")
