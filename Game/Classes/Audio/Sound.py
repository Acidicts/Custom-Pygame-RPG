import pygame


class Sound:
    def __init__(self, sound_file):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_file)

    def play(self, loops=-1):
        self.sound.play(loops=loops)

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume):
        self.sound.set_volume(volume)

    def get_length(self):
        return self.sound.get_length()
