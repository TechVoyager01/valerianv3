from src.chapters.chapter import *
from src.utils import battle
from src.utils.player import *
from src.utils.constants import *
from src.utils.enemies import chapter_4_enemies

def ruins_of_thaemus():
    """Function to start the Ruins of Thaemus encounter."""
    clear_terminal()
    print(chapter_4_story)
    battle(chapter_4_enemies, player_stats)