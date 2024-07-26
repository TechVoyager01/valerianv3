# imports of libraries
import os

# imports of functions
from game_title import display_game_title

# variables
gameplay = True

player_stats = {
    'Health': 100,
    'Attack': 10,
    'Defence': 5,
    'Potion': 3,
    'Elixir': 1,
    'Gold': 0,
    'location': 'Galador',
}

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

def print_player_stats(player_stats):
    print("\nValerian New Stats:")
    for key, value in player_stats.items():
        print(f"{key}: {value}")
    print()

def display_choice():
    draw_line()
    print(
        'Select an option: \n',
        'New Game: 1\n',
        'Load Game: 2\n',
        'Save & Exit: 3',
    )
    draw_line()

def battle_action():
    print('Battle Action')
    print(
        'Attack: 1\n',
        'Defend: 2\n',
        'Use Potion (20HP): 3\n',
        'Use Elixir (40HP): 4\n',
        'Run: 4\n',
    )

def print_travel_choice():
    print('Travel Options')
    print(
        'North: 1\n',
        'South: 2\n',
        'East: 3\n',
        'West: 4\n',
        'Return to Galador: 5\n',
    )

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

def lets_play():
    print('Lets Play')


# main
def main_gameplay():
    # display_game_title_with_lines() # add later
    # display_story() # add later
    while gameplay:
        clear_terminal()
        display_choice()

        user_choice = input('>  ')

        if user_choice == '1':
            draw_line()
            # prints origin story and first capter
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
            user_choice = input('Press Yes to continue')
            draw_line()
            if user_choice.lower() == 'yes':
                print_player_stats(player_stats)
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