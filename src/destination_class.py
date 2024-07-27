# here is where we can make classes for destinations and load it into a list which can be used in game.

class Destination:
    def __init__(self, name, description, direction, key_features, battle=None):
        self.name = name
        self. description = description
        self.direction = direction
        self.key_features = key_features
        self.battle = bool(battle)

    def display_destination(self):
        print(f'{self.name}'
              f'\n{self.description}'
              f'\n{self.direction}'
              f'\n{self.key_features}'
              f'\n{self.battle}')

    # this allows for function to be called without creating an instance of the class
    @staticmethod
    def append_to_list(lst, destination):
        lst.append(destination)

# Initialize list
destinations = []

# Create a Destination instance
plains = Destination(
    'Plains',
    'A vast open field with a few trees around',
    'East',
    False
)


# Append the instance to the list
Destination.append_to_list(destinations, plains)

# Verify the list
print(destinations)