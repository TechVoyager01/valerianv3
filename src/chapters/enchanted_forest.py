from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def enchanted_forest(player_stats, save_player_stats, main_gameplay):
    """Function to start the Enchanted Forest encounter."""
    clear_terminal()
    print(chapter_2_story.title)
    print(chapter_2_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_2_enemies, player_stats, save_player_stats, main_gameplay)