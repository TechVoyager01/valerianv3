import os

def save_player_stats(file_path, player_stats):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w') as file:
        for key, value in player_stats.items():
            file.write(f"{key}: {value}\n")
