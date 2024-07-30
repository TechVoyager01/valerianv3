from src.chapters.chapter import *
from src.utils import battle
from src.utils.player import *
from src.utils.constants import *
from src.utils.enemies import chapter_3_enemies

def treacherous_mountains():
    """Function to start the Treacherous Mountains encounter."""
    clear_terminal()
    print(chapter_3_story)
    battle(chapter_3_enemies, player_stats)