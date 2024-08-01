# src/chapters/treacherous_mountains.py
from src.load_game.load_game import *
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

# src/chapters/treacherous_mountains.py
def treacherous_mountains(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the treacherous mountains encounter."""
    clear_terminal()
    player_stats['current_chapter'] = 3
    if isinstance(player_stats, dict):
        player_stats.setdefault('current_enemy', 0)  # Ensure current_enemy is initialized
    else:
        raise TypeError("player_stats must be a dictionary")
    player_stats = load_player_stats('src/save_game/save.txt')
    print(f"Loading Chapter: {player_stats['current_chapter']}")  # Debugging statement
    print(chapter_3_story.title)
    print(chapter_3_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    print(f"Player stats before battle: {player_stats}")  # Debugging statement
    battle(chapter_3_enemies, player_stats, save_player_stats, main_gameplay)