import os

def load_player_stats(file_path):
    """Function to load the player's stats from a file."""
    player_stats = {}
    if not os.path.exists(file_path):
        print(f"Save file not found: {file_path}")
        return player_stats
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                player_stats[key] = int(value) if value.isdigit() else value
        print(f"Player stats loaded from {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return player_stats