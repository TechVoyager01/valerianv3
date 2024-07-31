# making a enemy class to easily create future enemies for valerian to fight
# you can take this class and add enemies to the enemies list and create chapters around these enemies
class Enemy:
    def __init__(self, id, encounter, name, description, appearance, abilities, weakness, location, chapter, health, attack, defence, gold, potion, elixir):
        self.id = id
        self.encounter = encounter
        self.name = name
        self.description = description
        self.appearance = appearance
        self.abilities = abilities
        self.weakness = weakness
        self.location = location
        self.chapter = chapter
        self.health = health
        self.attack = attack
        self.defence = defence
        self.gold = gold
        self.potion = potion
        self.elixir = elixir

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - {self.description}"

# example
# enemy1 = Enemy(
#     id=1,
#     encounter='In a dark alley, you encounter a rough-looking individual with a crude weapon. It is a Street Thug, a common criminal lurking in the shadows.',
#     name="Street Thug",
#     description="Common criminals lurking in the alleys of Galador.",
#     appearance="Rough-looking individuals with crude weapons.",
#     abilities="Quick attacks, can call for backup.",
#     weakness="Low health, susceptible to strong single attacks.",
#     location="Galador",
#     chapter=1,
#     health=20,
#     attack=5,
#     defence=3,
#     gold=10,
#     potion=1,
#     elixir=0
# )
#
# enemy_list = [enemy1]
#
# for enemy in enemy_list
#     print(enemy)