import pygame
import Game.utils as utils
import os 


class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        self.font = pygame.font.Font(
            os.path.join("Game", "Assets", "Fonts", "Rubik_80s_Fade", "Rubik80sFade-Regular.ttf"), 32)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        pass
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.display.update()
    
    def loading_screen(self):
        self.screen.fill((0, 0, 0))
        text = ["Wagoniser Studios", "Presents", "<Game-Title>"]
        display_text = ""
        for i in range(len(text)):
            for letter in text[i]:
                display_text += letter
            
                self.screen.fill((30, 30, 30))
            
                rendered = self.font.render(display_text, True, (255, 255, 255))
                self.screen.blit(rendered, (400 - rendered.get_width() // 2, 300 - rendered.get_height() // 2))
            
                pygame.event.pump()
                pygame.time.delay(200)
            
                pygame.display.update()
                pygame.event.pump()

            display_text = ""
            pygame.time.delay(200)
            pygame.event.pump()

        utils.fade(self.screen, (0, 0, 0), 50, 50)

        return None
    
    def run(self, argv):
        load_screen = True
        for arg in argv:
            if arg == "noload":
                load_screen = False

        if load_screen:
            self.loading_screen()

        while self.running:
            self.events()
            self.update()
            self.draw()