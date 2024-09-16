# This file contains the treacherous mountains encounter. Chapter 3

from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

# Chapter 3 story
def treacherous_mountains(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    clear_terminal()
    player_stats = load_player_stats('save_game_file/save_game/save.txt')
    draw_line()
    print('')
    typingPrint(chapter_3_story.title)
    typingPrint(chapter_3_story.description)
    draw_line()
    typingInput('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_3_enemies, player_stats, save_player_stats, main_gameplay)
    # save game after every chapter is completed
    save_player_stats('save_game_file/save_game/save.txt', player_stats)
# End of Chapter 3 story