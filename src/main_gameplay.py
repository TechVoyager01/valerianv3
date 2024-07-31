# main gameplay function to handle the gameplay loop
# imports
from src.chapters.glador import *
from src.utils.player import *

# variables
gameplay = True

def main_gameplay():

    global player_stats

    while gameplay:
        clear_terminal()
        display_choice()

        user_choice = input('>  ')

        if user_choice == '1':
            player_stats = reset_player_stats()
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
                glador(player_stats)
                break
            elif user_choice.lower() == 'no':
                print('Your current game will be saved')
                load_player_stats('load.txt')
                break
            break
        # still a work in progress
        elif user_choice == '2':
            print('Load Game')
            break
        # need to update this feature
        elif user_choice == '3':
            print('Save & Exit')
            save_player_stats('save.txt', player_stats)
            exit()
        elif user_choice == 'exit':
            print('Game Over')
            quit()