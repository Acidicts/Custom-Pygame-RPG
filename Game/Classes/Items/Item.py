import pygame


class Item:
    def __init__(self, name, description, image=pygame.Surface((16, 16))):
        self.name = name
        self.description = description
        self.image = image

    def use(self):
        pass

    def draw(self, surf, pos=(0, 0)):
        img = pygame.transform.scale(self.image, (32, 32))
        surf.blit(img, pos)
