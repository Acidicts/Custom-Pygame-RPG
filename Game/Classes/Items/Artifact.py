import Game.Classes.Items.Dynamic_Item as Dynamic_Item
import random

colours = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0), (200, 0, 200), (0, 200, 200)]
elements = {
    "fire": colours[0],
    "earth": colours[1],
    "water": colours[2],
    "air": colours[3],
    "light": colours[4],
    "dark": colours[5]
}


class Artifact(Dynamic_Item.DynamicItem):
    def __init__(self, name, description, element):
        clas = random.choice(["ring", "stone"])
        super().__init__(name, description, f"Game/Assets/Templates/{clas}_artifact.png", random.choice(colours), elements[element])
        print(elements[element])
        element = element

        self.colour = elements[element]
        self.type = type
        self.element = element
