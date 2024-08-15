# save_game_file/chapters/ruins_of_thaemus.py
from src.chapters import *
from src.load_game.load_game import *
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *
from src.chapters.end_game import *

def ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the ruins of Thaemus encounter."""
    clear_terminal()
    player_stats = load_player_stats('save_game_file/save_game/save.txt')
    draw_line()
    print('')
    print(chapter_4_story.title)
    print(chapter_4_story.description)
    draw_line()
    input('\nPress ENTER to continue...')
    clear_terminal()
    battle(chapter_4_enemies, player_stats, save_player_stats, main_gameplay)
    # does not get a chapter 5 until there is another added for now
    # jus be sure to player_stats['current_chapter'] = 5
    clear_terminal()
    end_game()
    input('\nPress ENTER to continue and start a Game...')
    reset_player_stats(player_stats)
    main_gameplay()