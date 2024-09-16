# function to reset player stats to initial values

def reset_player_stats(player_stats):
    """Reset player stats to initial values."""
    player_stats['Health'] = 100
    player_stats['Attack'] = 10
    player_stats['Defence'] = 5
    player_stats['Potion'] = 3
    player_stats['Elixir'] = 1
    player_stats['Gold'] = 0
    player_stats['location'] = 'Galador'
    player_stats['current_chapter'] = 1
    player_stats['current_enemy'] = 0
    return player_stats