# save_game_file/chapters/enchanted_forest.py
from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def enchanted_forest(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the enchanted forest encounter."""
    clear_terminal()
    player_stats = load_player_stats('save_game_file/save_game/save.txt')
    draw_line()
    print('')
    print(chapter_2_story.title)
    print(chapter_2_story.description)
    draw_line()
    input('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_2_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('save_game_file/save_game/save.txt', player_stats)


    # maybe creating a new if else statement to ensure the correct battle on the correct chapter when user loads game.