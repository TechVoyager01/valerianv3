def load_player_stats(file_path):
    """Function to load the player's stats from a file."""
    try:
        with open(file_path, 'r') as file:
            for item in file:
                key = item.split(':')[0].strip()
                value = item.split(':')[1].strip()
                player_stats[key] = value
                print(f"Player stats loaded from {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")