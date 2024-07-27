# imports of libraries
import os
from collections import ChainMap

# import random

# imports of functions
from game_title import display_game_title
# from destination_class import Destination
from travel import *

# variables
gameplay = True
play = True

# player stats
player_stats = {
    'Health': 100,
    'Attack': 10,
    'Defence': 5,
    'Potion': 3,
    'Elixir': 1,
    'Gold': 0,
    'location': 'Galador',
}
# enemies and their description
enemy_list = [
        {
            'id': 1,
            "name": "Stone Sentinel",
            "description": "Ancient golems created to guard Thaemus, now crushing intruders.",
            "appearance": "Massive figures made of stone and metal with glowing runes.",
            "abilities": "Immense strength, hurl boulders, create seismic shockwaves.",
            "weakness": "Slow, susceptible to agility-based attacks and magic disrupting runes.",
            "HP": 40,
            "Attack": 10,
            "Defence": 5,
            "Gold": 20,
            "Potion": 2
        },
        {
            'id': 2,
            "name": "Arcane Trickster",
            "description": "Rogue mages using forbidden magic, deceiving and trapping adventurers.",
            "appearance": "Hooded figures with glowing eyes, adorned with talismans.",
            "abilities": "Illusions, powerful spells, magical traps, summon spectral minions.",
            "weakness": "Overconfidence, illusions dispelled with clarity spells.",
            "HP": 50,
            "Attack": 15,
            "Defence": 6,
            "Gold": 40,
            "Potion": 3
        },
        {
            'id': 3,
            "name": "Shadow Wraith",
            "description": "Ghostly remnants of Thaemus's cursed inhabitants, haunting the ruins.",
            "appearance": "Ghostly figures with glowing eyes and tattered cloaks.",
            "abilities": "Phase through walls, become invisible, drain life force.",
            "weakness": "Vulnerable to light-based magic and enchanted weapons.",
            "HP": 60,
            "Attack": 20,
            "Defence": 7,
            "Gold": 50,
            "Potion": 4
        },
        {
            'id': 4,
            "name": "Forest Stalker",
            "description": "Predatory creatures that camouflage and ambush travelers in the forests.",
            "appearance": "Sleek, "
                          "eline-like with mottled fur, sharp claws, piercing eyes.",
            "abilities": "Stealth, climb trees, paralyzing bite.",
            "weakness": "Vulnerable to fire and loud noises.",
            "HP": 70,
            "Attack": 25,
            "Defence": 7,
            "Gold": 60,
            "Potion": 5
        }
    ]

# functions
# function to display a line
def draw_line():
    print("xX--------------------------------------Xx")

# function to clear the terminal screen
def clear_terminal():
    # Check the operating system and execute the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# function to display the game title
def display_game_title_with_lines():
    draw_line()
    display_game_title()
    draw_line()

# function to display the story line and what to encounter
def display_story():
    intro_text = """
    Welcome, brave adventurer, to the mystical world of Orius!

    In the heart of Orius lies the bustling city of Galador,
    where stories of ancient legends and forgotten treasures
    are whispered in every tavern and marketplace.
    Among these legends, one tale stands out above the rest—
    the legend of Thaemus, a once-great city now lost to time and myth.

    Centuries ago, Thaemus was the crown jewel of Orius,
    a city of unparalleled beauty and prosperity.
    Its citizens lived in peace and harmony,
    protected by a powerful artifact that granted eternal youth
    to those deemed worthy.
    However, as time passed, greed and jealousy grew
    within the hearts of the people.
    In their desperation to control the artifact's power,
    a curse befell the city, and it vanished into the shadows,
    hidden away from the world.

    You are Valerian, a young and curious explorer from Galador.
    Driven by tales of Thaemus and the promise of eternal youth,
    you decide to embark on a daring quest
    to uncover the secrets of the lost city.
    Your journey will take you through dense forests,
    treacherous mountains, and perilous ruins,
    where you will face trials that test your strength,
    wit, and courage.

    Your ultimate goal is to find the ancient artifact of Thaemus
    and prove yourself worthy of its power.
    But beware—the path is fraught with danger,
    and only the bravest and most cunning adventurers will succeed.
    Along the way, you will uncover the true history of Thaemus,
    meet allies who will aid you,
    and confront formidable foes who will stop at nothing
    to protect the secrets of the city.

    Are you ready to take up the challenge
    and embark on the quest of a lifetime?
    The fate of Thaemus and the promise of eternal youth await you!

    1. Prepare Yourself: Gather your wits and steel your nerves
       for the journey ahead. The path to Thaemus is not for the faint of heart.
    2. Meet the Sage: Seek out the old sage in Galador
       who holds the key to your quest.
       He will provide you with a mystical map and cryptic advice to guide you on your way.
    3. Embark on Your Journey: Leave the safety of Galador
       and venture into the wild, where trials and challenges await.
       Trust in your skills and the friends you meet along the way.

    Press Enter to begin your adventure...
    """
    print(intro_text)

# function to print player stats updates in battle
def print_player_stats(player_stats):
    print("\nValerian Stats:")
    for key, value in player_stats.items():
        print(f"{key}: {value}")

# function to display enemy stats in battle
def print_enemy_stats(enemy):
    print("\nEnemy Stats:")
    for key, value in enemy.items():
        if key not in ['id', 'name', 'description', 'appearance', 'abilities', 'weakness']:
            print(f"{key}: {value}")

# function to reset player stats
def reset_player_stats():
    return {
        'Health': 100,
        'Attack': 10,
        'Defence': 5,
        'Potion': 3,
        'Elixir': 1,
        'Gold': 0,
        'location': 'Galador',
    }

# function to display the user's choice, load game, new game, save and exit
def display_choice():
    draw_line()
    print(
        'Select an option: \n',
        'New Game: 1\n',
        'Load Game: 2\n',
        'Save & Exit: 3',
    )
    draw_line()

# function to display the battle action options, fight, defend, use potion, use elixir, run
def battle_action():
    print('Battle Action')
    print(
        '\nAttack: 1',
        '\nDefend: 2',
        '\nUse Potion (20HP): 3',
        '\nUse Elixir (40HP): 4',
        '\nRun: 4',
    )

# function to display the travel options, north, south, east, west  in development for later gameplay
# def print_travel_choice():
#     print('Travel Options')
#     print(
#         'North: 1\n',
#         'South: 2\n',
#         'East: 3\n',
#         'West: 4\n',
#         'Return to Galador: 5\n',
#     )

# function to make a random number between 0 and 10 to call battle function
# def random_number():
#     return random.randint(0, 10)

# function to display enemies

def display_enemies():
    for enemy in enemy_list:
        print(f"Name: {enemy['name']}")
        print(f"Description: {enemy['description']}")
        print(f"Appearance: {enemy['appearance']}")
        print(f"Abilities: {enemy['abilities']}")
        print(f"Weakness: {enemy['weakness']}")
        print(f"HP: {enemy['HP']}")
        print(f"Attack: {enemy['Attack']}")
        print(f"Defence: {enemy['Defence']}")
        print(f"Gold: {enemy['Gold']}")
        print(f"Potion: {enemy['Potion']}")
        print("-" * 40)

def display_single_enemy(enemy):
    print(f"Name: {enemy['name']}")
    print(f"Description: {enemy['description']}")
    print(f"Appearance: {enemy['appearance']}")
    print(f"Abilities: {enemy['abilities']}")
    print(f"Weakness: {enemy['weakness']}")
    print(f"HP: {enemy['HP']}")
    print(f"Attack: {enemy['Attack']}")
    print(f"Defence: {enemy['Defence']}")
    print(f"Gold: {enemy['Gold']}")
    print(f"Potion: {enemy['Potion']}")
    print("-" * 40)

# maybe put into own file later
# function to save player stats to load.txt
def save_player_stats(file_path, player_stats):
    try:
        with open(file_path, 'w') as file:
            for key, value in player_stats.items():
                file.write(f"{key}: {value}\n")
        print(f"Player stats saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# function to load player stats from load.txt
def load_player_stats(file_path):
    try:
        with open(file_path, 'r') as file:
            for item in file:
                key = item.split(':')[0].strip()
                value = item.split(':')[1].strip()
                player_stats[key] = value
                print(f"Player stats loaded from {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# function to call the battle function
def battle(enemy_list, player_stats):
    # Select the first enemy for the battle
    enemy = enemy_list[0]
    draw_line()
    print('You are at battle with', enemy['name'])
    draw_line()
    # battle loop
    while player_stats['Health'] > 0 and enemy['HP'] > 0:
        enemy = enemy_list[0]
        # functions to display player and enemy stats
        draw_line()
        print_player_stats(player_stats)
        draw_line()
        print_enemy_stats(enemy)
        draw_line()
        # function to display battle action options
        battle_action()
        draw_line()

        # Get player's choice
        choice = input('Choose your action: ')
        clear_terminal()

        if choice == '1':  # Attack
            print(f"You attack the {enemy['name']}!")
            enemy['HP'] -= player_stats['Attack']
            print(f"The {enemy['name']} has {enemy['HP']} HP left.")

        elif choice == '2':  # Defend
            print("You defend against the next attack.")
            player_stats['Defence'] += 5  # Temporary defense boost

        elif choice == '3':  # Use Potion
            if player_stats['Potion'] > 0:
                player_stats['Health'] += 20
                player_stats['Potion'] -= 1
                print("You used a potion. Your health is now", player_stats['Health'])
            else:
                print("You have no potions left!")

        elif choice == '4':  # Use Elixir
            if player_stats['Elixir'] > 0:
                player_stats['Health'] += 40
                player_stats['Elixir'] -= 1
                print("You used an elixir. Your health is now", player_stats['Health'])
            else:
                print("You have no elixirs left!")

        else:
            print("Invalid choice. Please select a valid action.")
            continue

        # Enemy's turn to attack
        if enemy['HP'] > 0:
            print(f"The {enemy['name']} attacks you!")
            player_stats['Health'] -= enemy['Attack'] - player_stats['Defence']
            print(f"Your health is now {player_stats['Health']}")

        # Reset temporary defense boost
        if choice == '2':
            player_stats['Defence'] -= 5

    # Check win/lose conditions
    if player_stats['Health'] <= 0:
        clear_terminal()
        print("You have been defeated!")
        main_gameplay()  # Restart the game if defeated
    elif enemy['HP'] <= 0:
        clear_terminal()
        print(f"You have defeated the {enemy['name']}!")

# temp glador encounter
def galador():
    clear_terminal()
    # change up the start but for now just make it work
    print("Welcome to Galador, the bustling capital city."
          "\nYour journey begins now..."
          "\nYou must defeat the four foes a head of you....."
          "\nYour battle begins now!"
          "\nFight!!!")
    battle(enemy_list, player_stats)


# main
def main_gameplay():
    global player_stats
    player_stats = reset_player_stats()  # Reset player stats at the start of the game

    while gameplay:
        clear_terminal()
        display_choice()

        user_choice = input('>  ')

        if user_choice == '1':
            draw_line()
            print('\nGreat News, Lets get you started.... '
                  '\nHere are some basic supplies to get to going on your adventure '
                  '\nNot much but it can get you where you need to go for now! \n'
                  '\nAnd so the First Chapter Begins..... \n'
                  '\nYou are Valerian, a young and curious explorer from Galador. '
                  '\nYou must find the hidden artifact of Thaemus to prove yourself worthy of its power. '
                  '\nYour journey will take you through dense forests, treacherous mountains, and perilous ruins. '
                  '\nAlong the way, you will uncover the true history of Thaemus, meet allies who will aid you, '
                  '\nand confront formidable foes who will stop at nothing to protect the secrets of the city. '
                  '\nAre you ready to take up the challenge and embark on the quest of a lifetime? \n')
            draw_line()

            user_choice = input('Press ENTER to continue or NO to SAVE and EXIT> ')

            if user_choice.lower() == '':
                draw_line()
                galador()
                break
            elif user_choice.lower() == 'no':
                print('Your current game will be saved')
                load_player_stats('load.txt')
                break
            break
        elif user_choice == '2':
            print('Load Game')
            break
        elif user_choice == '3':
            print('Save & Exit')
            break
        elif user_choice == 'exit':
            print('Game Over')
            break

main_gameplay()
