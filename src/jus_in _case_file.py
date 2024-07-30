# # imports of libraries
# import os
# import random
#
# # imports of functions
# from game_title import display_game_title
# from travel import *
# from src.utils.enemies import *
# from chapters.chapter import *
#
# # variables
# gameplay = True
#
# # player stats
# player_stats = {
#     'Health': 100,
#     'Attack': 10,
#     'Defence': 5,
#     'Potion': 3,
#     'Elixir': 1,
#     'Gold': 0,
#     'location': 'Galador',
# }
#
# # functions
# def draw_line():
#     """Function to print a decorative line."""
#     print("xX--------------------------------------Xx")
#
# def clear_terminal():
#     """Function to clear the terminal screen based on the operating system."""
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')
#
# def display_game_title_with_lines():
#     """Function to display the game title with decorative lines."""
#     draw_line()
#     display_game_title()
#     draw_line()
#
# def display_story():
#     """Function to display the introductory story of the game."""
#     intro_text = """
#     Welcome, brave adventurer, to the mystical world of Orius!
#     ...
#     Press Enter to begin your adventure...
#     """
#     print(intro_text)
#
# def print_player_stats(player_stats):
#     """Function to print the player's current stats."""
#     print("\nValerian Stats:\n")
#     for key, value in player_stats.items():
#         print(f"{key}: {value}")
#
# def print_enemy_stats(enemy):
#     """Function to print the current enemy's stats."""
#     print("\nEnemy Stats:\n")
#     for key, value in enemy.items():
#         if key not in ['id', 'name', 'description', 'appearance', 'abilities', 'weakness', 'location', 'encounter', 'chapter']:
#             print(f"{key}: {value}")
#     print('')
#
# def reset_player_stats():
#     """Function to reset the player's stats to the initial values."""
#     return {
#         'Health': 100,
#         'Attack': 10,
#         'Defence': 5,
#         'Potion': 3,
#         'Elixir': 1,
#         'Gold': 0,
#         'location': 'Galador\n',
#     }
#
# def display_choice():
#     """Function to display the main menu choices."""
#     draw_line()
#     print(
#         '\n',
#         'Select an option: \n',
#         '\n',
#         'New Game: 1\n',
#         'Load Game: 2\n',
#         'Save & Exit: 3',
#         '\n',
#     )
#     draw_line()
#
# def battle_action():
#     """Function to display the battle action choices."""
#     print('\nBattle Action')
#     print(
#         '\nAttack: 1',
#         '\nDefend: 2',
#         '\nUse Potion (20HP): 3',
#         '\nUse Elixir (40HP): 4\n',
#         '\nSave & Exit: 5\n',
#     )
#
# def display_enemies():
#     """Function to display the list of enemies."""
#     for enemy in enemy_list:
#         print(f"Name: {enemy['name']}")
#         print(f"Description: {enemy['description']}")
#         print(f"Appearance: {enemy['appearance']}")
#         print(f"Abilities: {enemy['abilities']}")
#         print(f"Weakness: {enemy['weakness']}")
#         print(f"HP: {enemy['HP']}")
#         print(f"Attack: {enemy['Attack']}")
#         print(f"Defence: {enemy['Defence']}")
#         print(f"Gold: {enemy['Gold']}")
#         print(f"Potion: {enemy['Potion']}")
#         print("-" * 40)
#
# def display_single_enemy(enemy):
#     """Function to display a single enemy's details."""
#     print(f"Name: {enemy['name']}")
#     print(f"Description: {enemy['description']}")
#     print(f"Appearance: {enemy['appearance']}")
#     print(f"Abilities: {enemy['abilities']}")
#     print(f"Weakness: {enemy['weakness']}")
#     print(f"HP: {enemy['HP']}")
#     print(f"Attack: {enemy['Attack']}")
#     print(f"Defence: {enemy['Defence']}")
#     print(f"Gold: {enemy['Gold']}")
#     print(f"Potion: {enemy['Potion']}")
#     print("-" * 40)
#
# def battle_option_enemy(enemy):
#     """Function to handle the enemy's battle actions."""
#     random_num = random.randint(1, 4)
#     if enemy['Health'] > 0:
#         if random_num == 1:
#             print('Your enemy has chosen to attack')
#             print(f"The {enemy['name']} attacks you!")
#             player_stats['Health'] -= enemy['Attack'] - player_stats['Defence']
#             print(f"Your health is now {player_stats['Health']}")
#         elif random_num == 2:
#             print(f"The {enemy['name']} defends against you!")
#             enemy['Defence'] += 5
#             print(f"The {enemy['name']} increased their defence to {enemy['Defence']}.")
#         elif random_num == 3:
#             if enemy['Potion'] > 0:
#                 print('Your enemy has chosen to use  a potion')
#                 enemy['Health'] += 20
#                 enemy['Potion'] -= 1
#                 print(f"The {enemy['name']} used a potion. They have {enemy['Potion']} potions left.")
#             else:
#                 print('The enemy has no potions left!')
#         elif random_num == 4:
#             if enemy['Elixir'] > 0:
#                 print('Your enemy has chosen to use an elixir')
#                 enemy['Health'] += 40
#                 enemy['Elixir'] -= 1
#                 print(f"The {enemy['name']} used an elixir. They have {enemy['Elixir']} elixirs left.")
#             else:
#                 print('The enemy has no elixirs left!')
#     else:
#         print('There is a problem in the logic of the enemy fighting you')
#
# def battle_option_player(player_stats, enemy):
#     """Function to handle the player's battle actions."""
#     choice = input('Choose your action: ')
#     clear_terminal()
#
#     if choice == '1':
#         print(f"You attack the {enemy['name']}!")
#         enemy['Health'] -= player_stats['Attack']
#         print(f"The {enemy['name']} has {enemy['Health']} HP left.")
#     elif choice == '2':
#         print("You defend against the next attack.")
#         player_stats['Defence'] += 5
#     elif choice == '3':
#         if player_stats['Potion'] > 0:
#             player_stats['Health'] += 20
#             player_stats['Potion'] -= 1
#             print("You used a potion. Your health is now", player_stats['Health'])
#         else:
#             print("You have no potions left!")
#     elif choice == '4':
#         if player_stats['Elixir'] > 0:
#             player_stats['Health'] += 40
#             player_stats['Elixir'] -= 1
#             print("You used an elixir. Your health is now", player_stats['Health'])
#         else:
#             print("You have no elixirs left!")
#     elif choice == '5':
#         save_player_stats('save.txt', player_stats)
#         print("Game saved. Exiting...")
#         exit()
#     else:
#         print("Invalid choice. Please select a valid action.")
#
# def save_player_stats(file_path, player_stats):
#     """Function to save the player's stats to a file."""
#     try:
#         with open(file_path, 'w') as file:
#             for key, value in player_stats.items():
#                 file.write(f"{key}: {value}\n")
#         print(f"Player stats saved to {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# def load_player_stats(file_path):
#     """Function to load the player's stats from a file."""
#     try:
#         with open(file_path, 'r') as file:
#             for item in file:
#                 key = item.split(':')[0].strip()
#                 value = item.split(':')[1].strip()
#                 player_stats[key] = value
#                 print(f"Player stats loaded from {file_path}")
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# def battle(enemy_list, player_stats):
#     """Function to handle the battle sequence between the player and enemies."""
#     while player_stats['Health'] > 0 and len(enemy_list) > 0:
#         enemy = enemy_list[0]
#         enemy_encounter = enemy["encounter"]
#         draw_line()
#         print(enemy_encounter)
#         draw_line()
#         print('You are at battle with', enemy['name'])
#         draw_line()
#
#         while player_stats['Health'] > 0 and enemy['Health'] > 0:
#             draw_line()
#             print_player_stats(player_stats)
#             draw_line()
#             print_enemy_stats(enemy)
#             draw_line()
#             battle_action()
#             draw_line()
#
#             battle_option_player(player_stats, enemy)
#             battle_option_enemy(enemy)
#
#         if player_stats['Health'] <= 0:
#             clear_terminal()
#             print("You have been defeated!")
#             main_gameplay()
#             return
#         elif enemy['Health'] <= 0:
#             clear_terminal()
#             print(f"You have defeated the {enemy['name']}!")
#             player_stats['Gold'] += enemy['Gold']
#             enemy_list.pop(0)
#
#     if len(enemy_list) == 0:
#         print("Congratulations! You have defeated all enemies! \nOnto the next chapter!")
#         next_chapter(1)
#
# def update_player_location(player_stats, chapter):
#     """Function to update the player's location based on the current chapter."""
#     chapter_locations = {
#         1: 'Galador',
#         2: 'Enchanted Forest',
#         3: 'Treacherous Mountains',
#         4: 'Ruins of Thaemus'
#     }
#     player_stats['location'] = chapter_locations.get(chapter, 'Unknown Location')
#
# def next_chapter(current_chapter):
#     """Function to transition to the next chapter after defeating all enemies."""
#     print("You have completed the first chapter. Prepare for the next chapter!")
#     global player_stats, enemy_list
#     player_stats['Health'] = 100
#     player_stats['Potion'] += 2
#     player_stats['Elixir'] += 1
#     current_chapter += 1
#     update_player_location(player_stats, current_chapter)
#     print(f"Your new location is {player_stats['location']}")
#
# def galador():
#     """Function to start the Galador encounter."""
#     clear_terminal()
#     print(chapter_1_story)
#     input('Press ENTER to continue...')
#     clear_terminal()
#     battle(chapter_1_enemies, player_stats)
#
# def enchanted_forest():
#     """Function to start the Enchanted Forest encounter."""
#     clear_terminal()
#     print(chapter_2_story)
#     battle(chapter_2_enemies, player_stats)
#
# def treacherous_mountains():
#     """Function to start the Treacherous Mountains encounter."""
#     clear_terminal()
#     print(chapter_3_story)
#     battle(chapter_3_enemies, player_stats)
#
# def ruins_of_thaemus():
#     """Function to start the Ruins of Thaemus encounter."""
#     clear_terminal()
#     print(chapter_4_story)
#     battle(chapter_4_enemies, player_stats)
#
# def main_gameplay():
#     """Main function to handle the gameplay loop."""
#     global player_stats
#     player_stats = reset_player_stats()
#
#     while gameplay:
#         clear_terminal()
#         display_choice()
#
#         user_choice = input('>  ')
#
#         if user_choice == '1':
#             draw_line()
#             print('\nGreat News, Lets get you started.... '
#                   '\nHere are some basic supplies to get to going on your adventure '
#                   '\nNot much but it can get you where you need to go for now! \n'
#                   '\nAnd so the First Chapter Begins..... \n'
#                   '\nYou are Valerian, a young and curious explorer from Galador. '
#                   '\nYou must find the hidden artifact of Thaemus to prove yourself worthy of its power. '
#                   '\nYour journey will take you through dense forests, treacherous mountains, and perilous ruins. '
#                   '\nAlong the way, you will uncover the true history of Thaemus, meet allies who will aid you, '
#                   '\nand confront formidable foes who will stop at nothing to protect the secrets of the city. '
#                   '\nAre you ready to take up the challenge and embark on the quest of a lifetime? \n')
#             draw_line()
#
#             user_choice = input('Press ENTER to continue or NO to SAVE and EXIT> ')
#
#             if user_choice.lower() == '':
#                 draw_line()
#                 galador()
#                 break
#             elif user_choice.lower() == 'no':
#                 print('Your current game will be saved')
#                 load_player_stats('load.txt')
#                 break
#             break
#         elif user_choice == '2':
#             print('Load Game')
#             break
#         elif user_choice == '3':
#             print('Save & Exit')
#             save_player_stats('save.txt', player_stats)
#             exit()
#         elif user_choice == 'exit':
#             print('Game Over')
#             break
#
# main_gameplay()