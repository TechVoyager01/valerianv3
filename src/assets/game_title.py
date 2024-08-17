# os is a terminal interaction library
import os

def display_game_title(file_path='assets/Game_Title'):
    # this is done so that the function can work in the terminal
    try:
        if not os.path.isfile(file_path): # os path
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r') as file:
            game_title = file.read()
            print(game_title)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")