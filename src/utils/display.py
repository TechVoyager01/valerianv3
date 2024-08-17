from src.utils.typing_effect import *
# functions to print/display all the game features, story and stats
# the function to allow save_game and go back to main menu
def display_story():
    """Function to display the introductory story of the game."""
    intro_text = """
    Welcome, brave adventurer, to the mystical world of Orius!
    ...
    Press Enter to begin your adventure...
    """
    typingPrint(intro_text)

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

def print_enemy_stats(enemy):
    """Function to print the enemy's stats."""
    print(" ")
    print(f"Enemy: {enemy['name']}")
    print(" ")
    print(f"Health: {enemy['Health']}")
    print(f"Attack: {enemy['Attack']}")
    print(f"Defence: {enemy['Defence']}")
    print(f"Potion: {enemy['Potion']}")
    print(f"Elixir: {enemy['Elixir']}")
    print(" ")

def print_player_stats(player_stats):
    """Function to print the player's current stats."""
    print("\nValerian Stats:\n")
    for key, value in player_stats.items():
        print(f"{key}: {value}")

# the function to allow save_game and go back to main menu
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

def draw_line():
    """Function to print a decorative line."""
    print("xX--------------------------------------Xx")

def display_game_title_with_lines(gametitle):
    """Function to display the game title with decorative lines."""
    draw_line()
    print(gametitle)
    draw_line()

def display_choice():
    """Display the game choices."""
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