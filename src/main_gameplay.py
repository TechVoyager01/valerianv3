# This file contains the main gameplay loop for the game. It allows the player to start a new game, load a saved game, or exit the game.

# Importing the necessary functions and classes
from src.chapters.glador import glador
from src.chapters.enchanted_forest import enchanted_forest
from src.chapters.treacherous_mountains import treacherous_mountains
from src.chapters.ruins_of_thaemus import ruins_of_thaemus
from src.player import reset_player_stats
from src.save_game.save_game import save_player_stats
from src.utils.display import display_choice, draw_line
from src.utils.clear_terminal import clear_terminal
from src.battle.battle import battle
from src.assets.game_title import display_game_title
from src.load_game.load_game import *
from src.utils.typing_effect import *

# Global variable to control the gameplay loop
gameplay = True

# Main gameplay loop
def main_gameplay():

    # player stats, health, potions, elixir, gold, location, current chapter, current enemy
    player_stats = {
        'Health': 100,
        'Attack': 10,
        'Defence': 5,
        'Potion': 3,
        'Elixir': 1,
        'Gold': 0,
        'location': 'Galador',
        'current_chapter': 0,
        'current_enemy': 0
    }

    # Main gameplay loop
    while gameplay:

        clear_terminal()
        display_game_title()
        typingInput('You are now playing Valerian and the Quest for Thaemus. Press enter to continue...')
        clear_terminal()

        display_choice()

        user_choice = input('>  ')

        # Check the user choice
        if user_choice == '1':

            player_stats = reset_player_stats(player_stats)  # Reset player stats
            # Save the player stats to a file before starting a new chapter
            draw_line()
            text1 = ('\nGreat News, Lets get you started.... '
                  '\nHere are some basic supplies to get to going on your adventure '
                  '\nNot much but it can get you where you need to go for now! \n'
                  '\nAnd so the First Chapter Begins..... \n'
                  '\nYou are Valerian, a young and curious explorer from Galador. '
                  '\nYou must find the hidden artifact of Thaemus to prove yourself worthy of its power. '
                  '\nYour journey will take you through dense forests, treacherous mountains, and perilous ruins. '
                  '\nAlong the way, you will uncover the true history of Thaemus, meet allies who will aid you, '
                  '\nand confront formidable foes who will stop at nothing to protect the secrets of the city. '
                  '\nAre you ready to take up the challenge and embark on the quest of a lifetime? \n')
            typingPrint(text1)
            typingPrint('lets get you started....\n')
            draw_line()

            user_choice = typingInput('\nPress ENTER to continue or NO to SAVE and EXIT> ')

            # Check the user choice
            if user_choice.lower() == '':
                glador(player_stats, save_player_stats, main_gameplay, battle)
                enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
                treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
                # Add end game text and art here...
                main_gameplay()
            elif user_choice.lower() == 'no':
                typingPrint('Your current game will be saved')
                save_player_stats('save_game_file/save_game/save.txt', player_stats)
                main_gameplay()
        elif user_choice == '2':
            # temp load game logic follow continue_ game for more
            # Load the player stats from a file before loading up new chapter to continue the game
            path = 'save_game_file/save_game/save.txt'
            player_stats = load_player_stats('save_game_file/save_game/save.txt')  # Load player stats
            draw_line()
            clear_terminal()
            print(f"Continuing from Chapter: {player_stats['current_chapter']}") # testing statement, currently loading wrong chapter, always loading chapter 1
            typingInput('Press enter to continue....')
            if player_stats['current_chapter'] == 1:
                # insert a new function to play all chapters in sequence (folder save_game_file/chapters), save game after each chapter
                glador(player_stats, save_player_stats, main_gameplay, battle)
                enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
                treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
            elif player_stats['current_chapter'] == 2:
                enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
                treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
            elif player_stats['current_chapter'] == 3:
                treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
            elif player_stats['current_chapter'] == 4:
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
            main_gameplay()
                # Add end game text and art here...
            main_gameplay()
        elif user_choice == '3':
            typingPrint('And your outta here!!!!!')
            quit()
        else:
            draw_line()
            typingPrint('Invalid choice, please try again')
            draw_line()
            main_gameplay()