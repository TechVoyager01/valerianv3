# function to clear the terminal screen based on the operating system

# import the necessary packages
import sys, os

# clear the terminal.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')