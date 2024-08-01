# main gameplay function to handle the gameplay loop
# imports
from src.chapters.glador import *
from src.chapters.enchanted_forest import *
from src.chapters.treacherous_mountains import *
from src.chapters.ruins_of_thaemus import *
from src.load_game.continue_game import *
from src.save_game.save_game import *
from src.utils import *

# variables
gameplay = True

player_stats = {
        'Health': 100,
        'Attack': 10,
        'Defence': 5,
        'Potion': 3,
        'Elixir': 1,
        'Gold': 0,
        'location': 'Galador\n',
        'current_chapter': 1,
        'current_enemy': 0
    }

def main_gameplay():

    global player_stats

    while gameplay:
        clear_terminal()
        display_choice()

        user_choice = input('>  ')

        if user_choice == '1':
            player_stats = reset_player_stats(player_stats)
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
                glador(player_stats, save_player_stats, main_gameplay)
                enchanted_forest(player_stats, save_player_stats, main_gameplay)
                treacherous_mountains(player_stats, save_player_stats, main_gameplay)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay)
                break
            elif user_choice.lower() == 'no':
                print('Your current game will be saved')
                save_player_stats('src/save_game/save.txt', player_stats)
                main_gameplay()
        elif user_choice == '2':
            # Load the player stats from a file
            continue_game()
            main_gameplay()
        elif user_choice == '3':
            print('And your outta here!!!!!')
            quit()
        else:
            draw_line()
            print('Invalid choice, please try again')
            draw_line()
            main_gameplay()