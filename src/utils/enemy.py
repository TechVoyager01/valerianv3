from src.utils.constants import *
from src.utils.battle import *
from src.main_gameplay import *

def print_enemy_stats(enemy):
    """Function to print the current enemy's stats."""
    print("\nEnemy Stats:\n")
    for key, value in enemy.items():
        if key not in ['id', 'name', 'description', 'appearance', 'abilities', 'weakness', 'location', 'encounter', 'chapter']:
            print(f"{key}: {value}")
    print('')\

def battle(enemy_list, player_stats):
    """Function to handle the battle sequence between the player and enemies."""
    while player_stats['Health'] > 0 and len(enemy_list) > 0:
        enemy = enemy_list[0]
        enemy_encounter = enemy["encounter"]
        draw_line()
        print(enemy_encounter)
        draw_line()
        print('You are at battle with', enemy['name'])
        draw_line()

        while player_stats['Health'] > 0 and enemy['Health'] > 0:
            draw_line()
            print_player_stats(player_stats)
            draw_line()
            print_enemy_stats(enemy)
            draw_line()
            battle_action()
            draw_line()

            battle_option_player(player_stats, enemy)
            battle_option_enemy(enemy)

        if player_stats['Health'] <= 0:
            clear_terminal()
            print("You have been defeated!")
            main_gameplay()
            return
        elif enemy['Health'] <= 0:
            clear_terminal()
            print(f"You have defeated the {enemy['name']}!")
            player_stats['Gold'] += enemy['Gold']
            enemy_list.pop(0)

    if len(enemy_list) == 0:
        print("Congratulations! You have defeated all enemies! \nOnto the next chapter!")