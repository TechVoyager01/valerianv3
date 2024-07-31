def save_player_stats(file_path, player_stats):
    """Function to save_game the player's stats to a file."""
    try:
        with open(file_path, 'w') as file:
            for key, value in player_stats.items():
                file.write(f"{key}: {value}\n")
        print(f"Player stats saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")