# functions to help the battle mechanics
import os, random

from src.main_gameplay import main_gameplay
from src.utils.constants import clear_terminal, save_player_stats

def print_enemy_stats(enemy):
    """Function to print the current enemy's stats."""
    print("\nEnemy Stats:\n")
    for key, value in enemy.items():
        if key not in ['id', 'name', 'description', 'appearance', 'abilities', 'weakness', 'location', 'encounter', 'chapter']:
            print(f"{key}: {value}")
    print('')

def battle_option_enemy(enemy):
    """Function to handle the enemy's battle actions."""
    global player_stats
    random_num = random.randint(1, 4)
    if enemy['Health'] > 0:
        if random_num == 1:
            print('Your enemy has chosen to attack')
            print(f"The {enemy['name']} attacks you!")
            player_stats['Health'] -= enemy['Attack'] - player_stats['Defence']
            print(f"Your health is now {player_stats['Health']}")
        elif random_num == 2:
            print(f"The {enemy['name']} defends against you!")
            enemy['Defence'] += 5
            print(f"The {enemy['name']} increased their defence to {enemy['Defence']}.")
        elif random_num == 3:
            if enemy['Potion'] > 0:
                print('Your enemy has chosen to use  a potion')
                enemy['Health'] += 20
                enemy['Potion'] -= 1
                print(f"The {enemy['name']} used a potion. They have {enemy['Potion']} potions left.")
            else:
                print('The enemy has no potions left!')
        elif random_num == 4:
            if enemy['Elixir'] > 0:
                print('Your enemy has chosen to use an elixir')
                enemy['Health'] += 40
                enemy['Elixir'] -= 1
                print(f"The {enemy['name']} used an elixir. They have {enemy['Elixir']} elixirs left.")
            else:
                print('The enemy has no elixirs left!')
    else:
        print('There is a problem in the logic of the enemy fighting you')

def battle_option_player(player_stats, enemy):
    """Function to handle the player's battle actions."""
    choice = input('Choose your action: ')
    clear_terminal()

    if choice == '1':
        print(f"You attack the {enemy['name']}!")
        enemy['Health'] -= player_stats['Attack']
        print(f"The {enemy['name']} has {enemy['Health']} HP left.")
    elif choice == '2':
        print("You defend against the next attack.")
        player_stats['Defence'] += 5
    elif choice == '3':
        if player_stats['Potion'] > 0:
            player_stats['Health'] += 20
            player_stats['Potion'] -= 1
            print("You used a potion. Your health is now", player_stats['Health'])
        else:
            print("You have no potions left!")
    elif choice == '4':
        if player_stats['Elixir'] > 0:
            player_stats['Health'] += 40
            player_stats['Elixir'] -= 1
            print("You used an elixir. Your health is now", player_stats['Health'])
        else:
            print("You have no elixirs left!")
    elif choice == '5':
        save_player_stats('save.txt', player_stats)
        print("Game saved. Exiting...")
        main_gameplay()
    else:
        print("Invalid choice. Please select a valid action.")

def reset_player_stats():
    """Function to reset the player's stats to the initial values."""
    return {
        'Health': 100,
        'Attack': 10,
        'Defence': 5,
        'Potion': 3,
        'Elixir': 1,
        'Gold': 0,
        'location': 'Galador\n',
    }

# the function to allow save and go back to main menu
def battle_action():
    """Function to display the battle action choices."""
    print('\nBattle Action')
    print(
        '\nAttack: 1',
        '\nDefend: 2',
        '\nUse Potion (20HP): 3',
        '\nUse Elixir (40HP): 4\n',
        '\nSave & Exit: 5\n',
    )