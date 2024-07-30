from src.chapters.chapter import *
from src.utils import battle
from src.utils.player import *
from src.utils.constants import *
from src.utils.enemies import chapter_2_enemies

def enchanted_forest():
    """Function to start the Enchanted Forest encounter."""
    clear_terminal()
    print(chapter_2_story)
    battle(chapter_2_enemies, player_stats)