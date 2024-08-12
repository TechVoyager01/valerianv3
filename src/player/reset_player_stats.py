# Function to reset player stats
def reset_player_stats(player_stats):
    """Reset player stats to initial values."""
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
    for key, value in player_stats.items():
        player_stats.setdefault(key, value)
    return player_stats