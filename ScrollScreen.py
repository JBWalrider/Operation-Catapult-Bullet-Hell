import pygame
from pygame.locals import *

class ScrollScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\\Background.png")
        self.rect = self.image.get_rect()
        self.dy = 2
        self.rect.bottom = 800
        
    def update(self):
        self.rect.y += self.dy
        if self.rect.bottom >= 1600:
            self.rect.bottom = 800