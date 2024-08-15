# this function helps the chosen option fro the player to attack or heal, also has the option to exit and save
from src.utils.display import *

def battle_option_player(player_stats, enemy, clear_terminal, save_player_stats, main_gameplay):
    """Function to handle the player's battle actions."""
    choice = input('\nChoose your action: ')
    clear_terminal()
    draw_line()
    if choice == '1':
        print(f"You attack the {enemy['name']}!")
        enemy['Health'] -= player_stats['Attack']
        print(f"The {enemy['name']} has {enemy['Health']} HP left.")
        draw_line()
    elif choice == '2':
        print("You defend against the next attack.")
        player_stats['Defence'] += 5
        draw_line()
    elif choice == '3':
        if player_stats['Potion'] > 0:
            player_stats['Health'] += 20
            player_stats['Potion'] -= 1
            print("You used a potion. Your health is now", player_stats['Health'])
            draw_line()
        else:
            print("You have no potions left!")
            draw_line()
    elif choice == '4':
        if player_stats['Elixir'] > 0:
            player_stats['Health'] += 40
            player_stats['Elixir'] -= 1
            print("You used an elixir. Your health is now", player_stats['Health'])
            draw_line()
        else:
            print("You have no elixirs left!")
            draw_line()
    elif choice == '5':
        save_player_stats('save_game_file/save_game/save.txt', player_stats)
        draw_line()
        print("Game saved. Exiting...")
        draw_line()
        exit()
    else:
        print("Invalid choice. Please select a valid action.")