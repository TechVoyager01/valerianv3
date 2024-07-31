from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def treacherous_mountains(player_stats, save_player_stats, main_gameplay):
    """Function to start the Treacherous Mountains encounter."""
    clear_terminal()
    print(chapter_3_story.title)
    print(chapter_3_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_3_enemies, player_stats, save_player_stats, main_gameplay)