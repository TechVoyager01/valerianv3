# src/save_game/load_game.py

def continue_game():
    # Logic to load the player stats from a saved file
    with open('save_game_file/save_game/save.txt', 'r') as file:
        player_stats = eval(file.read())
    return player_stats