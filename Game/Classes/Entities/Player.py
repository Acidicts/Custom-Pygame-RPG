import Game.classes.Entities.Entity as Entity


class Player(Entity):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)

        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
