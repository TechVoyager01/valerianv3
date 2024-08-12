# src/load_game/load_game.py
def load_player_stats(file_path):
    """Load player stats from a file."""
    player_stats = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            player_stats[key] = int(value) if value.isdigit() else value
    return player_stats