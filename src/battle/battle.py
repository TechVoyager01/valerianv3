# This file contains the main battle logic for the game and how players and enemies will interact with one another.

# Imports from files and function.
from src.player.battle_option_player import battle_option_player
from src.enemy.battle_options_enemy import battle_option_enemy
from src.player.reset_player_stats import reset_player_stats
from src.utils.clear_terminal import clear_terminal
from src.utils.display import *
from src.utils.typing_effect import *

# main function to handle the battle sequence between the player and enemies.
def battle(enemy_list, player_stats, save_player_stats, main_gameplay):
    # while loops to keep the game running until the player or enemy health reaches 0.
    while player_stats['Health'] > 0 and len(enemy_list) > 0: # so the player can play if the health is above 0
        # initializing variables.
        enemy = enemy_list[0]
        enemy_encounter = enemy["encounter"]
        draw_line()
        typingPrint(enemy_encounter)
        draw_line()
        typingPrint('You are at battle with', enemy['name'])
        draw_line()

        # while loop to keep the battle going until either the player or enemy health reaches 0.
        while player_stats['Health'] > 0 and enemy['Health'] > 0:
            print_player_stats(player_stats)
            print('')
            draw_line()
            print_enemy_stats(enemy)
            draw_line()
            battle_action()
            draw_line()

            battle_option_player(player_stats, enemy, clear_terminal, save_player_stats, main_gameplay)
            battle_option_enemy(enemy, player_stats)

        # parameters if the users health reaches zero or the enemy health reaches zero.
        if player_stats['Health'] <= 0:
            clear_terminal()
            typingPrint("You have been defeated!")
            typingPrint("Game Over!")
            reset_player_stats(player_stats)
            main_gameplay()
            return
        elif enemy['Health'] <= 0:
            clear_terminal()
            # loot function to give the player gold, health, potions, and elixirs if the user defeats the enemy.
            draw_line()
            typingPrint(f"You have defeated the {enemy['name']}!")
            player_stats['Gold'] += enemy['Gold']
            player_stats['Health'] += 20
            player_stats['Potion'] += 1
            player_stats['Elixir'] += 1
            player_stats['current_enemy'] += 1
            save_player_stats('save_game_file/save_game/save.txt', player_stats)
            enemy_list.pop(0)
    # insures the player moves into the next chapter if all enemies are defeated.
    if len(enemy_list) == 0:
        player_stats['current_chapter'] += 1
        typingPrint("Congratulations! You have defeated all enemies! \nOnto the next chapter!")