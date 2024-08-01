# src/chapters/enchanted_forest.py
from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

# src/chapters/enchanted_forest.py
def enchanted_forest(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the enchanted forest encounter."""
    clear_terminal()
    player_stats['current_chapter'] = 2
    if isinstance(player_stats, dict):
        player_stats.setdefault('current_enemy', 0)  # Ensure current_enemy is initialized
    else:
        raise TypeError("player_stats must be a dictionary")
    player_stats = load_player_stats('src/save_game/save.txt')
    print(f"Loading Chapter: {player_stats['current_chapter']}")  # Debugging statement
    print(chapter_2_story.title)
    print(chapter_2_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    print(f"Player stats before battle: {player_stats}")  # Debugging statement
    battle(chapter_2_enemies, player_stats, save_player_stats, main_gameplay)