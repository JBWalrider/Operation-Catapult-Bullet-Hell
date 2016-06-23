import pygame
from pygame.locals import *
from Controller import *

class Menu:

    class Option:

        hovered = False
        font = None
    
        def __init__(self, text, pos, font, surface):
            self.text = text
            self.pos = pos
            self.font = font
            self.surface = surface
            self.set_rect()
            self.draw()
            music = pygame.mixer.music.load("sounds/menuMusic.mp3")
            pygame.mixer.music.play()
                
        def draw(self):
            self.set_rend()
            self.surface.blit(self.rend, self.rect)
            
        def set_rend(self):
            self.rend = self.font.render(self.text, True, self.get_color())
            
        def get_color(self):
            if self.hovered:
                return (255, 255, 255)
            else:
                return (100, 100, 100)
            
        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

    def menustart(self):
        while True:
            pygame.event.pump()
            pygame.mouse.set_visible(1)
            for option in self.options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if self.options[0].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(0)
                        pygame.mixer.music.stop()
                        self.c.start()
                        return
                if self.options[1].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(1)
                        return
                if self.options[2].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(0)
                        return
                    
    def __init__(self, controller):
        pygame.init()
        menu_font = pygame.font.Font(None, 40)

        self.c = controller
        self.surface = controller.screen

        start = self.Option("START", (200, 540), menu_font, self.surface)
        credits = self.Option("CREDITS", (182, 580), menu_font, self.surface)
        exit = self.Option("EXIT", (210, 620), menu_font, self.surface)
        
        self.options = [start, credits, exit]
        self.TitleScreen = pygame.image.load("images/Title.png")
        self.TitleScreen.convert()
        self.surface.blit(self.TitleScreen, (0, 0))
        
    def start(self):
        self.menustart()
        #self.surface.blit(self.TitleScreen, (0,0))
        
    
