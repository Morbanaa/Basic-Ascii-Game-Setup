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
            self.game_map.append(row)

    # Renders world each frame of game
    def render_game(self):
        pass

    # Sets screen for next frame
    def clear_move_cursor():
        sys.stdout.write("\033[H")
        sys.stdout.flush()

class Player():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos