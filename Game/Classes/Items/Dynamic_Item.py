import Game.Classes.Items.Item as Item
import pygame


class DynamicItem(Item.Item):
    def __init__(self, name, description, template, colour_1, colour_2):
        super().__init__(name, description, pygame.Surface((16, 16)))
        self.colours = {1: colour_1, 2: colour_2}
        colours = {1: (55, 71, 79), 2: (38, 50, 56)}
        self.template = {"template": template, "set_colours": colours}

        self.make_image()

    def use(self):
        pass

    def make_image(self):
        # Load the template image
        image = pygame.image.load(self.template["template"]).convert()

        # Get the pixel array of the image
        pixel_array = pygame.PixelArray(image)

        # Iterate through the pixel array and replace colors
        for key, color in self.template["set_colours"].items():
            pixel_array.replace(self.template["set_colours"][key], self.colours[key])

        # Convert the pixel array back to a surface
        self.image = pixel_array.make_surface()
        self.image.set_colorkey((0, 0, 0))
        self.image.convert()

        del pixel_array
