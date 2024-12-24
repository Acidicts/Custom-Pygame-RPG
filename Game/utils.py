import pygame
import os

BASE_IMG_PATH = "Game/Assets/"


def fade(surface, color, delay=30, break_early=255):
    for a in range(break_early):
    
        surf = pygame.Surface(surface.get_size())
        surf.fill(color)
        surf.set_alpha(a)
        surface.blit(surf, (0, 0))
    
        pygame.display.update()
    
        pygame.time.delay(delay)

    # Returns True to say it is complete
    print("Fade complete")
    return True


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + str(img_name)))
    return images


class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images))
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]
