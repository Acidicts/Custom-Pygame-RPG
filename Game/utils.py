import pygame
import os

BASE_IMG_PATH = "Game/Assets/"


def flip_img_list(img_list):
    return [pygame.transform.flip(img, True, False) for img in img_list]


def load_spritesheet(path, img_size, row_names):
    sheet = pygame.image.load(BASE_IMG_PATH + path).convert()
    sheet.set_colorkey((0, 0, 0))  # Set the color key for transparency
    sprites = {}

    for y in range(sheet.get_height() // img_size[1]):
        row_sprites = []
        for x in range(sheet.get_width() // img_size[0]):
            surf = pygame.Surface(img_size).convert()
            surf.set_colorkey((0, 0, 0))
            surf.blit(sheet, (0, 0), (x * img_size[0], y * img_size[1], img_size[0], img_size[1]))

            blank = True
            for px in range(surf.get_height()):
                for py in range(surf.get_width()):
                    if not surf.get_at((px, py)) == (0, 0, 0):
                        blank = False
                        break

            if not blank:
                row_sprites.append(surf)

        try:
            sprites[row_names[y]] = row_sprites
        except IndexError:
            sprites[str(y)] = row_sprites

    return sprites


def fade(surface, color, delay=30, break_early=255):
    for a in range(break_early):

        surf = pygame.Surface(surface.get_size())
        surf.fill(color)
        surf.set_alpha(a)
        surface.blit(surf, (0, 0))

        pygame.display.update()

        pygame.time.delay(delay)

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
