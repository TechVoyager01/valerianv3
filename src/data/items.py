class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def use(self):
        print(f"Using {self.name}")

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super().__init__(name, description, value)
        self.damage = damage

    def use(self):
        print(f"Swinging {self.name} for {self.damage} damage")

class Armor(Item):
    def __init__(self, name, description, value, defense):
        super().__init__(name, description, value)
        self.defense = defense

    def use(self):
        print(f"Wearing {self.name} for {self.defense} defense")