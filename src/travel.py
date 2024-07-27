# temp travel options for testing

def start_game(self):
    input()  # Wait for the player to press Enter
    print("\nYour journey begins now..."
          "\nYou must defeat the four foes a head of you....."
          "\nYour battle begins now!"
          "\nFight!!!")
    self.navigate_areas()


def navigate_areas(self):
    while self.player.alive:
        if self.current_area == "Galador":
            self.galador()
        elif self.current_area == "Enchanted Forest":
            self.enchanted_forest()
        elif self.current_area == "Treacherous Mountains":
            self.treacherous_mountains()
        elif self.current_area == "Ruins of Thaemus":
            self.ruins_of_thaemus()
        else:
            print("Unknown area. Game over.")
            break


def galador(self):
    print("Welcome to Galador, the bustling capital city."
          "\nYour journey begins now..."
          "\nYou must defeat the four foes a head of you....."
          "\nYour battle begins now!"
          "\nFight!!!")

    # Add more interactions and transitions to the next area
    self.current_area = "Enchanted Forest"  # Example transition


def enchanted_forest(self):
    print("You are now in the Enchanted Forest. Beware of its magical inhabitants.")
    # Add more interactions and transitions to the next area
    self.current_area = "Treacherous Mountains"  # Example transition


def treacherous_mountains(self):
    print("You are traversing the Treacherous Mountains. Proceed with caution.")
    # Add more interactions and transitions to the next area
    self.current_area = "Ruins of Thaemus"  # Example transition


def ruins_of_thaemus(self):
    print("You have reached the Ruins of Thaemus. The artifact awaits you.")
    # Add more interactions and the final confrontation