# Teddy Rodd
# Morbanaa Studios
# Basic Ascii Game Setup

import keyboard

class Player():
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
            
    # Player Movement
    def update_player(self,game_map):
        # Move Up
        if keyboard.is_pressed("W") and game_map[self.ypos -1][self.xpos] != "@":
            self.ypos -= 1
        # Move Down
        if keyboard.is_pressed("S") and game_map[self.ypos + 1][self.xpos] != "@":
            self.ypos += 1
        # Move Left
        if keyboard.is_pressed("A") and game_map[self.ypos][self.xpos -1] != "@":
            self.xpos -= 1
        # Move Right
        if keyboard.is_pressed("D") and game_map[self.ypos][self.xpos +1] != "@":
            self.xpos += 1