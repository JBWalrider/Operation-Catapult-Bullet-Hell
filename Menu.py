import pygame
from pygame.locals import *
from Controller import *

c = Controller(500, 800)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bullet Hell")

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
menu_font = pygame.font.Font(None, 40)
options = [Option("START", (180, 400))]

def menustart():
    while True:
        pygame.event.pump()
        screen.fill((0, 0, 0))
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if options[0].hovered == True:
                if event.type == MOUSEBUTTONDOWN:
                    c.start()
menustart()