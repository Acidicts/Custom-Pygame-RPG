import pygame


class SpriteGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        max_z = 0

        for sprite in self.sprites():
            if sprite.z > max_z:
                max_z = sprite.z

        for z in range(max_z + 1):
            for sprite in self.sprites():
                if sprite.z == z:
                    screen.blit(sprite.image, sprite.rect.topleft)

    def update(self, dt):
        for sprite in self.sprites():
            sprite.update(dt)

