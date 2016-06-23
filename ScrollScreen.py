import pygame
from pygame.locals import *

class ScrollScreen(pygame.sprite.Sprite):
    def __init__(self, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\\Background.png")
        self.rect = self.image.get_rect()
        self.dy = 2
        self.rect.bottom = screen_height
        self.height = screen_height
        
    def update(self):
        self.rect.y += self.dy
        if self.rect.bottom >= 2*self.height:
            self.rect.bottom = self.height