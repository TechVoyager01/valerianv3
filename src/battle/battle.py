from src.enemy.battle_options_enemy import *
from src.player import *
from src.utils.clear_terminal import *
from src.utils.display import *

def battle(enemy_list, player_stats, save_player_stats, main_gameplay):
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

            battle_option_player(player_stats, save_player_stats, main_gameplay)
            battle_option_enemy(enemy, player_stats)

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