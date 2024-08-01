# src/chapters/ruins_of_thaemus.py
from src.load_game.load_game import load_player_stats
from src.battle.battle import *
from src.chapters.chapter import *
from src.enemy.enemies import *
from src.utils.display import *
from src.utils.clear_terminal import *

# src/chapters/ruins_of_thaemus.py
def ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, current_enemy=0):
    """Function to start the ruins of Thaemus encounter."""
    clear_terminal()
    player_stats['current_chapter'] = 4
    if isinstance(player_stats, dict):
        player_stats.setdefault('current_enemy', 0)  # Ensure current_enemy is initialized
    else:
        raise TypeError("player_stats must be a dictionary")
    player_stats = load_player_stats('src/save_game/save.txt')
    print(f"Loading Chapter: {player_stats['current_chapter']}")  # Debugging statement
    print(chapter_4_story.title)
    print(chapter_4_story.description)
    draw_line()
    input('Press ENTER to continue...')
    clear_terminal()
    print(f"Player stats before battle: {player_stats}")  # Debugging statement
    battle(chapter_4_enemies, player_stats, save_player_stats, main_gameplay)