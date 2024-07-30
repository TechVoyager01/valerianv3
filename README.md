# Valerian Adventure Game

## Overview
Valerian Adventure Game is a text-based adventure game where players embark on a quest through various chapters, encountering enemies and uncovering the secrets of the ancient city of Thaemus.

## Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/TechVoyager01/valerianv3.git
    cd valerianv3
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Game
To start the game, run the following command:
```sh
python src/main.py

## File structure of the project

valerianv3/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── game_title.py
│   ├── travel.py
│   ├── enemies.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── display.py
│   │   ├── file_operations.py
│   │   ├── battle.py
│   │   ├── player.py
│   │   ├── enemy.py
│   │   ├── game_state.py
│   │   ├── constants.py
│   ├── chapters/
│   │   ├── __init__.py
│   │   ├── chapters.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── quests.py
│   ├── assets/
│   │   ├── __init__.py
│   │   ├── images/
│   │   ├── sounds/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py
│   │   ├── test_battle.py
│   │   ├── test_file_operations.py
├── README.md
├── requirements.txt
├── setup.py

## To run test do the following....

python -m unittest discover -s src/tests
