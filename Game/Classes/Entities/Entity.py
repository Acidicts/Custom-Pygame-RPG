import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, z=0):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.width = width
        self.height = height

        self.z = z

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
