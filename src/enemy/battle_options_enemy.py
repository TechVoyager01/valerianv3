# this file contains the function that handles the enemy's battle actions and stats.

# import random as the random module is needed to generate random numbers for the enemy's actions.
import random

# import the draw_line function from the display module to display a line after each action.
from src.utils.display import *

# function to handle the enemy's battle actions.
def battle_option_enemy(enemy, player_stats):
    # initalizing a random number to determine the enemy's action
    random_num = random.randint(1, 4)
    # parameters on the enemy's action.
    if enemy['Health'] > 0:
        if random_num == 1:
            print('Your enemy has chosen to attack')
            print(f"The {enemy['name']} attacks you!")
            player_stats['Health'] -= enemy['Attack'] - player_stats['Defence']
            print(f"Your health is now {player_stats['Health']}")
            draw_line()
        elif random_num == 2:
            print(f"The {enemy['name']} defends against you!")
            enemy['Defence'] += 5
            print(f"The {enemy['name']} increased their defence to {enemy['Defence']}.")
            draw_line()
        elif random_num == 3:
            if enemy['Potion'] > 0:
                print('Your enemy has chosen to use a potion')
                enemy['Health'] += 20
                enemy['Potion'] -= 1
                print(f"The {enemy['name']} used a potion. They have {enemy['Potion']} potions left.")
                draw_line()
            else:
                print('The enemy has no potions left!')
                draw_line()
        elif random_num == 4:
            if enemy['Elixir'] > 0:
                print('Your enemy has chosen to use an elixir')
                enemy['Health'] += 40
                enemy['Elixir'] -= 1
                print(f"The {enemy['name']} used an elixir. They have {enemy['Elixir']} elixirs left.")
                draw_line()
            else:
                draw_line()
                print('The enemy has no elixirs left!')
    else:
        print('There is a problem in the logic of the enemy fighting you')
        draw_line()