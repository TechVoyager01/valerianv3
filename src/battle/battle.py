# save_game_file/battle/battle.py
from src.player.battle_option_player import battle_option_player
from src.enemy.battle_options_enemy import battle_option_enemy
from src.player.reset_player_stats import reset_player_stats
from src.utils.clear_terminal import clear_terminal
from src.utils.display import *

# the function needs some touch ups and some more features to be added
def battle(enemy_list, player_stats, save_player_stats, main_gameplay):
    """Function to handle the battle sequence between the player and enemies."""
    while player_stats['Health'] > 0 and len(enemy_list) > 0: # so the player can play if the health is above 0

        enemy = enemy_list[0]
        enemy_encounter = enemy["encounter"]
        draw_line()
        print(enemy_encounter)
        draw_line()
        print('You are at battle with', enemy['name'])
        draw_line()

        while player_stats['Health'] > 0 and enemy['Health'] > 0:
            print_player_stats(player_stats)
            draw_line()
            print_enemy_stats(enemy)
            draw_line()
            battle_action()
            draw_line()

            battle_option_player(player_stats, enemy, clear_terminal, save_player_stats, main_gameplay)
            battle_option_enemy(enemy, player_stats)

        if player_stats['Health'] <= 0:
            clear_terminal()
            print("You have been defeated!")
            print("Game Over!")
            reset_player_stats(player_stats)
            main_gameplay()
            return
        elif enemy['Health'] <= 0:
            clear_terminal()
            # add loot function here in the future
            print(f"You have defeated the {enemy['name']}!")
            player_stats['Gold'] += enemy['Gold']
            player_stats['Health'] += 20
            player_stats['Potion'] += 1
            player_stats['Elixir'] += 1
            player_stats['current_enemy'] += 1
            save_player_stats('save_game_file/save_game/save.txt', player_stats)
            enemy_list.pop(0)

    if len(enemy_list) == 0:
        player_stats['current_chapter'] += 1
        print("Congratulations! You have defeated all enemies! \nOnto the next chapter!")