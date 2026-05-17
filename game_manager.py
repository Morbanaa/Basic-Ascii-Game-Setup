# Teddy Rodd
# Morbanaa Studios
# Basic Ascii Game Setup

import sys
import keyboard
from player import Player

# Colors
GREEN        = '\033[32m'
# Reset Color
ENDC = '\033[0m'

class Game_Manager():
    def __init__(self,game_width,game_height):
        self.game_width = game_width
        self.game_height = game_height
        self.player = Player(game_width//2,game_height//2)
        self.game_map = []

    # Creates world onces at start of game
    def world_gen(self):
        for y in range(self.game_height):
            row = []
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.game_map.append(row)

    # Renders world each frame of game
    def render_game(self):
        # Update
        self.player.update_player(self.game_map) # Passes in game map

        for y in range(self.game_height):
            for x in range(self.game_width):
                if y == self.player.ypos and x == self.player.xpos:
                    print(f"{GREEN}P{ENDC}",end="")
                else:
                    print(self.game_map[y][x],end="")
            print()

    # Sets screen for next frame
    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()
    
   