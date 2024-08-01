# src/chapters/glador.py
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

# src/chapters/glador.py
def glador(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the Glador encounter."""
    clear_terminal()
    player_stats['current_chapter'] = 1
    if isinstance(player_stats, dict):
        player_stats.setdefault('current_enemy', 0)  # Ensure current_enemy is initialized
    else:
        raise TypeError("player_stats must be a dictionary")
    print(f"Loading Chapter: {player_stats['current_chapter']}")  # Debugging statement
    print(chapter_1_story.title)
    print(chapter_1_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    print(f"Player stats before battle: {player_stats}")  # Debugging statement
    battle(chapter_1_enemies, player_stats, save_player_stats, main_gameplay)