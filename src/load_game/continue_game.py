# src/load_game/continue_game.py
from src.load_game.load_game import load_player_stats

def continue_game():
    """Load the player stats from a file and return them."""
    return load_player_stats('src/save_game/save.txt')


# this function needs to be fixed, it needs to be called into main gameplay to continue the game from the last saved point
# for example

# elif user_choice == '2':
# # Load the player stats from a file before loading up new chapter to continue the game
# player_stats = continue_game()
# draw_line()
# print(
#     f"Continuing from Chapter: {player_stats['current_chapter']}")  # testing statement, currently loading wrong chapter, always loading chapter 1
# if player_stats['current_chapter'] == 1:
#     # insert a new function to play all chapters in sequence (folder src/chapters), save game after each chapter
#     glador(player_stats, save_player_stats, main_gameplay, battle)
#     enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
#     treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
#     ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
#     break
# elif player_stats['current_chapter'] == 2:
#     enchanted_forest(player_stats, save_player_stats, main_gameplay, battle)
#     treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
#     ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
# elif player_stats['current_chapter'] == 3:
#     treacherous_mountains(player_stats, save_player_stats, main_gameplay, battle)
#     ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
# elif player_stats['current_chapter'] == 4:
#     ruins_of_thaemus(player_stats, save_player_stats, main_gameplay, battle)
#     # Add end game text and art here...