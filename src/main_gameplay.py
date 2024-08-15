# save_game_file/main_gameplay.py
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

gameplay = True


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

    while gameplay:

        clear_terminal()
        display_game_title()
        input('You are now playing Valerian and the Quest for Thaemus. Press enter to continue...')
        clear_terminal()

        display_choice()

        user_choice = input('>  ')

        if user_choice == '1':

            player_stats = reset_player_stats(player_stats)  # Reset player stats

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
            print('lets get you started....\n')
            draw_line()

            user_choice = input('\nPress ENTER to continue or NO to SAVE and EXIT> ')

            if user_choice.lower() == '':
                glador(player_stats, save_player_stats, main_gameplay, battle)
                enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
                treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
                ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
                # Add end game text and art here...
                main_gameplay()
            elif user_choice.lower() == 'no':
                print('Your current game will be saved')
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
            input('Press enter to continue....')
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
            print('And your outta here!!!!!')
            quit()
        else:
            draw_line()
            print('Invalid choice, please try again')
            draw_line()
            main_gameplay()