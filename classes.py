import sys

class Game_Manager():
    def __init__(self,game_width,game_height):
        self.game_width = game_width
        self.game_height = game_height
        self.player = Player(game_width//2,game_height//2)

    # Creates world onces at start of game
    def world_gen(self):
        pass

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