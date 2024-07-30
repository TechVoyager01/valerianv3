from src.chapters.chapter import chapter_1_story
from src.utils import battle
from src.utils.constants import *
from src.utils.enemies import chapter_1_enemies

def galador(player_stats):
    """Function to start the Galador encounter."""
    clear_terminal()
    print(chapter_1_story.title)
    print(chapter_1_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    battle(chapter_1_enemies, player_stats)