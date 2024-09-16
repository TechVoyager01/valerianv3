# Load game functions

# load player stats from file.
def load_player_stats(file_path):
    player_stats = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            player_stats[key] = int(value) if value.isdigit() else value
    return player_stats