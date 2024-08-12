# save_game_file/save_game/save_game.py
import os

def save_player_stats(file_path, player_stats):
    """Save player stats to a file."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as file:
        for key, value in player_stats.items():
            file.write(f"{key}={value}\n")