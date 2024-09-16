# This file contains functions to display the game features, story and stats

# import the typing effect function
from src.utils.typing_effect import *

# the function to print intro to the game.
def display_story():
    intro_text = """
    Welcome, brave adventurer, to the mystical world of Orius!
    ...
    Press Enter to begin your adventure...
    """
    typingPrint(intro_text)

# the function to choose the players action in battle.
def battle_action():
    print('\nBattle Action')
    print(
        '\nAttack: 1',
        '\nDefend: 2',
        '\nUse Potion (20HP): 3',
        '\nUse Elixir (40HP): 4\n',
        '\nSave & Exit: 5\n',
    )

# the function to print the enemy stats
def print_enemy_stats(enemy):
    print(" ")
    print(f"Enemy: {enemy['name']}")
    print(" ")
    print(f"Health: {enemy['Health']}")
    print(f"Attack: {enemy['Attack']}")
    print(f"Defence: {enemy['Defence']}")
    print(f"Potion: {enemy['Potion']}")
    print(f"Elixir: {enemy['Elixir']}")
    print(" ")

# the function prints the player stats
def print_player_stats(player_stats):
    print("\nValerian Stats:\n")
    for key, value in player_stats.items():
        print(f"{key}: {value}")

# the function to allow save_game and go back to main menu
def battle_action():
    print('\nBattle Action')
    print(
        '\nAttack: 1',
        '\nDefend: 2',
        '\nUse Potion (20HP): 3',
        '\nUse Elixir (40HP): 4\n',
        '\nSave & Exit: 5\n',
    )

# the function to print a line of dashes
def draw_line():
    print("xX--------------------------------------Xx")

# function to print the game title with decorative lines
def display_game_title_with_lines(gametitle):
    draw_line()
    print(gametitle)
    draw_line()

# function to display the main menu
def display_choice():
    choices = (
        '\nSelect an option: \n'
        '\nNew Game: 1\n'
        'Load Game: 2\n'
        'Exit: 3\n'
        '\n'
    )
    draw_line()
    typingPrint(choices)
    draw_line()