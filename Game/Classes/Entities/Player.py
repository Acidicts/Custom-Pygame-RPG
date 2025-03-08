import pygame

from Game.Classes.Entities.Entity import Entity
from Game.utils import *
from Game.Setting.Player import *


class Player(Entity):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)

        self.speed = 150
        self.velocity = pygame.Vector2(0, 0)

        self.sprites = load_spritesheet("Images/Player/Player_Old/Player.png", (32, 32), anim_names)
        self.images = {
            "idle_down": Animation(self.sprites["idle_down"], 5),
            "idle_right": Animation(self.sprites["idle_direction"], 5),
            "idle_up": Animation(self.sprites["idle_up"], 5),
            "idle_left": Animation(flip_img_list(self.sprites["idle_direction"]), 5),
            "walk_down": Animation(self.sprites["walk_down"], 5),
            "walk_right": Animation(self.sprites["walk_direction"], 5),
            "walk_up": Animation(self.sprites["walk_up"], 5),
            "walk_left": Animation(flip_img_list(self.sprites["walk_direction"]), 5)
        }

        self.animation_name = "idle_down"
        self.animation = self.images[self.animation_name]

    def controls(self):
        keys = pygame.key.get_pressed()

        self.velocity.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.velocity.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize()

    def animation_update(self):
        if self.velocity.x > 0:
            self.animation_name = "walk_right"
        if self.velocity.x < 0:
            self.animation_name = "walk_down"
        if self.velocity.y < 0 and self.velocity.x == 0:
            self.animation_name = "walk_up"
        if self.velocity.y > 0 and self.velocity.x == 0:
            self.animation_name = "walk_down"

        if self.velocity.y == 0 and self.velocity.x == 0 and "idle" not in self.animation_name:
            anim = self.animation_name.split("_")[1]
            self.animation_name = "idle_" + anim

        self.animation = self.images[self.animation_name]

    def update(self, dt):
        self.controls()
        self.animation_update()

        self.rect.x += self.velocity.x * self.speed * dt
        self.rect.y += self.velocity.y * self.speed * dt

        self.animation.update()
        self.image = self.animation.img()
