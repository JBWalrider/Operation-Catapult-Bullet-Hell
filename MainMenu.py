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

    def repaint(self):
        self.surface.blit(self.TitleScreen, (0, 0))

    def menuStart(self):
        while True:
            pygame.event.pump()
            pygame.mouse.set_visible(True)
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
                        pygame.mouse.set_visible(True)

                        difficultyFont = pygame.font.Font(None, 40)
                        
                        easy = self.Option("EASY", (200, 540), difficultyFont, self.surface)
                        med = self.Option("MEDIUM", (184, 580), difficultyFont, self.surface)
                        hard = self.Option("HARD", (197, 620), difficultyFont, self.surface)
                        diffi = 0

                        self.difficultyOptions = [easy,med,hard]
                        self.difficultyScreen = pygame.image.load("images/Title.png")
                        self.difficultyScreen.convert()
                        self.surface.blit(self.difficultyScreen, (0, 0))
                        difficult = True     
                        while difficult == True:
                            pygame.event.pump()
                            pygame.mouse.set_visible(True)
                            for option in self.difficultyOptions:
                                if option.rect.collidepoint(pygame.mouse.get_pos()):
                                    option.hovered = True
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return
                                if self.difficultyOptions[0].hovered == True:
                                    if event.type == MOUSEBUTTONDOWN:
                                        diffi = 1000
                                        self.c.setdiff(diffi)
                                        action = self.c.start()
                                        if action == "Exit":
                                            self.repaint()
                                            pygame.mixer.music.load("sounds/menuMusic.mp3")
                                            pygame.mixer.music.play(-1)
                                            difficult = False
                                            break
                                        elif action == "Quit":
                                            return
                                if self.difficultyOptions[1].hovered == True:
                                    if event.type == MOUSEBUTTONDOWN:
                                        diffi = 750
                                        self.c.setdiff(diffi)
                                        action = self.c.start()
                                        if action == "Exit":
                                            self.repaint()
                                            pygame.mixer.music.load("sounds/menuMusic.mp3")
                                            pygame.mixer.music.play(-1)
                                            difficult = False
                                            break
                                        elif action == "Quit":
                                            return
                                if self.difficultyOptions[2].hovered == True:
                                    if event.type == MOUSEBUTTONDOWN:
                                        diffi = 500
                                        self.c.setdiff(diffi)
                                        action = self.c.start()
                                        if action == "Exit":
                                            self.repaint()
                                            pygame.mixer.music.load("sounds/menuMusic.mp3")
                                            pygame.mixer.music.play(-1)
                                            difficult = False
                                            break
                                        elif action == "Quit":
                                            return
                if self.options[1].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(True)

                        instructFont = pygame.font.Font(None, 40)
                        
                        back = self.Option("BACK", (200, 580), instructFont, self.surface)
        
                        self.instructOptions = [back]
                        self.instructScreen = pygame.image.load("images/Instructions.png")
                        self.instructScreen.convert()
                        self.surface.blit(self.instructScreen, (0, 0))
                        
                        instructed = True     
                        while instructed == True:
                            pygame.event.pump()
                            pygame.mouse.set_visible(True)
                            for option in self.instructOptions:
                                if option.rect.collidepoint(pygame.mouse.get_pos()):
                                    option.hovered = True
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return
                                if self.instructOptions[0].hovered == True:
                                    if event.type == MOUSEBUTTONDOWN:
                                        instructed = False
                    self.surface.blit(self.TitleScreen, (0, 0))
                    
                if self.options[2].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(True)

                        creditFont = pygame.font.Font(None, 40)
                        
                        back = self.Option("BACK", (200, 580), creditFont, self.surface)
        
                        self.creditOptions = [back]
                        self.CreditsScreen = pygame.image.load("images/Credits.png")
                        self.CreditsScreen.convert()
                        self.surface.blit(self.CreditsScreen, (0, 0))
                        
                        credited = True     
                        while credited == True:
                            pygame.event.pump()
                            pygame.mouse.set_visible(True)
                            for option in self.creditOptions:
                                if option.rect.collidepoint(pygame.mouse.get_pos()):
                                    option.hovered = True
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return
                                if self.creditOptions[0].hovered == True:
                                    if event.type == MOUSEBUTTONDOWN:
                                        credited = False
                    self.surface.blit(self.TitleScreen, (0, 0))
                        
                if self.options[3].hovered == True:
                    if event.type == MOUSEBUTTONDOWN:
                        pygame.mouse.set_visible(True)
                        return
                    
    def __init__(self, controller):

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        menuMusic = pygame.mixer.music.load("sounds/menuMusic.mp3")
        pygame.mixer.music.play(-1) 
        menuFont = pygame.font.Font(None, 40)

        self.c = controller
        self.surface = controller.screen

        start = self.Option("START", (200, 540), menuFont, self.surface)
        instructions = self.Option("INSTRUCTIONS", (138, 580), menuFont, self.surface)
        credits = self.Option("CREDITS", (182, 620), menuFont, self.surface)
        exit = self.Option("EXIT", (210, 660), menuFont, self.surface)
        
        self.options = [start, instructions, credits, exit]
        self.TitleScreen = pygame.image.load("images/Title.png")
        self.TitleScreen.convert()
        self.surface.blit(self.TitleScreen, (0, 0))
        
    def start(self):
        self.menuStart()
        
    
