# Teddy Rodd
# Morbanaa Studios
# Basic Ascii Game Setup

from classes import Game_Manager

def main():
    game_manager = Game_Manager(80,25) # Pass in Width Height
    game_manager.world_gen()
    while True:
        game_manager.update_player()
        game_manager.render_game()
        game_manager.clear_move_cursor()


if __name__ == "__main__":
    main()
