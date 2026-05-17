# Teddy Rodd
# Morbanaa Studios
# Basic Ascii Game Setup

import time
from classes import Game_Manager

def main():
    game_speed = .05 # Smaller number = faster game speed
    game_manager = Game_Manager(80,25) # Pass in Width Height
    game_manager.world_gen()
    while True:
        # Render
        game_manager.render_game()

        # Util
        time.sleep(game_speed) # Game Clock
        game_manager.clear_move_cursor() # Moves cursor to top of console


if __name__ == "__main__":
    main()
