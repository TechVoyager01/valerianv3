# src/chapters/glador.py
from src.load_game.load_game import load_player_stats
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def glador(player_stats, save_player_stats, main_gameplay, battle, current_enemy=0):
    """Function to start the enchanted forest encounter."""
    clear_terminal()
    print(chapter_1_story.title)
    print(chapter_1_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_1_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('src/save_game/save.txt', player_stats)