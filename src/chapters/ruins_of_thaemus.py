from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def ruins_of_thaemus(player_stats, save_player_stats, main_gameplay):
    """Function to start the Ruins of Thaemus encounter."""
    clear_terminal()
    print(chapter_4_story.title)
    print(chapter_4_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_4_enemies, player_stats, save_player_stats, main_gameplay)