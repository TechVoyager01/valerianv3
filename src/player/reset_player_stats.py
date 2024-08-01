def reset_player_stats(player_stats):
    """Function to reset player stats to default values."""
    default_stats = {
        'Health': 100,
        'Attack': 10,
        'Defence': 5,
        'Gold': 0,
        'Potion': 0,
        'Elixir': 0,
        'current_chapter': 1,
        'current_enemy': 0  # Initialize current_enemy
    }
    for key, value in default_stats.items():
        player_stats.setdefault(key, value)
    return player_stats