# This is the main file to run the game

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_gameplay import main_gameplay

def main():
    main_gameplay()

if __name__ == "__main__":
    main()