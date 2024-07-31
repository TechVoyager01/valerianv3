from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

def glador(player_stats, save_player_stats, main_gameplay):
    """Function to start the Glador encounter."""
    clear_terminal()
    print(chapter_1_story.title)
    print(chapter_1_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_1_enemies, player_stats, save_player_stats, main_gameplay)