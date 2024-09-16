# This file contains the ruins of Thaemus chapter. the final chapter for now.

from src.load_game.load_game import *
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *
from src.utils.typing_effect import *
from src.chapters.end_game import *

# Chapter 4: Ruins of Thaemus gameplay.
def ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    clear_terminal()
    player_stats = load_player_stats('save_game_file/save_game/save.txt')
    draw_line()
    print('')
    typingPrint(chapter_4_story.title)
    typingPrint(chapter_4_story.description)
    draw_line()
    typingInput('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_4_enemies, player_stats, save_player_stats, main_gameplay)
    clear_terminal()
    end_game()
    input('\nPress ENTER to continue and start a Game...')
    reset_player_stats(player_stats)
    main_gameplay()