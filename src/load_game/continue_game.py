# src/load_game/continue_game.py
# Function to continue the game from the last saved state
from src import main_gameplay
from src.load_game.load_game import *
from src.save_game.save_game import *
from src.player.reset_player_stats import *

def continue_game():
    try:
        # Load the player stats from a file
        player_stats = load_player_stats('src/save_game/save.txt')
        print(f"Loaded player stats: {player_stats}")  # Debugging statement
        # Ensure player_stats has all necessary keys
        player_stats = reset_player_stats(player_stats)
        print(f"Player stats after reset: {player_stats}")  # Debugging statement
        # Resume the game from the last saved state
        current_chapter = player_stats.get('current_chapter', 1)
        current_enemy = player_stats.get('current_enemy', 0)
        if current_chapter == 1:
            from src.chapters.glador import glador
            glador(player_stats, save_player_stats, main_gameplay, current_enemy)
        elif current_chapter == 2:
            from src.chapters.enchanted_forest import enchanted_forest
            enchanted_forest(player_stats, save_player_stats, main_gameplay, current_enemy)
        elif current_chapter == 3:
            from src.chapters.treacherous_mountains import treacherous_mountains
            treacherous_mountains(player_stats, save_player_stats, main_gameplay, current_enemy)
        elif current_chapter == 4:
            from src.chapters.ruins_of_thaemus import ruins_of_thaemus
            ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, current_enemy)
    except Exception as e:
        print(f"An error occurred: {e}")