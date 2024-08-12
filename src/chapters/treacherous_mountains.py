# src/chapters/treacherous_mountains.py
from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def treacherous_mountains(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the treacherous mountains encounter."""
    clear_terminal()
    player_stats = load_player_stats('src/save_game/save.txt')
    print(chapter_3_story.title)
    print(chapter_3_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_3_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('src/save_game/save.txt', player_stats)