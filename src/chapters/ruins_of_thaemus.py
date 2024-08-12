# save_game_file/chapters/ruins_of_thaemus.py
from src.chapters import end_game
from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the ruins of Thaemus encounter."""
    clear_terminal()
    player_stats = load_player_stats('save_game_file/save_game/save.txt')
    print(chapter_4_story.title)
    print(chapter_4_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_4_enemies, player_stats, save_player_stats, main_gameplay)
    end_game()
    # save game after every chapter is completed
    save_player_stats('save_game_file/save_game/save.txt', player_stats)