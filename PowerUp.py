import pygame, math
from pygame.locals import *
from Bullet import *


class PowerUp(pygame.sprite.Sprite):

    
    def __init__(self, pos, pType):
        super().__init__()
        self.image = pygame.image.load("images\\Shield_PowerUp.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.radius = 17
        self.pType = pType

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)

    def power(self, ship):
        if self.pType == 0:
            ship.giveShield(10)
      
