import sys

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
        for y in range(self.game_height):
            for x in range(self.game_width):
                print(self.game_map[y][x],end="")
            print()

    # Sets screen for next frame
    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()

class Player():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos