# this function is used to load the player stats from the saved file.

def continue_game():

    player_stats = {}
    try:
        with open('src/save_game/save.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key in ['Health', 'Attack', 'Defence', 'Potion', 'Elixir', 'Gold', 'current_chapter', 'current_enemy']:
                    player_stats[key] = int(value)
                else:
                    player_stats[key] = value

    # file error handling and resets the player stats if the file is not found.
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
        player_stats = {
            'Health': 100,
            'Attack': 10,
            'Defence': 5,
            'Potion': 3,
            'Elixir': 1,
            'Gold': 0,
            'location': 'Galador',
            'current_chapter': 1,
            'current_enemy': 0
        }
    return player_stats