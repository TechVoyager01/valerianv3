# save_game_file/chapters/glador.py
from src.load_game.load_game import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def glador(player_stats, save_player_stats, main_gameplay, battle, current_enemy=0):
    """Function to start the enchanted forest encounter."""
    clear_terminal()
    draw_line()
    print(chapter_1_story.title)
    print(chapter_1_story.description)
    draw_line()
    input('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_1_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('save_game_file/save_game/save.txt', player_stats)