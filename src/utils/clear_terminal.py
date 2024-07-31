import sys, os

def clear_terminal():
    """Function to clear the terminal screen based on the operating system."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')