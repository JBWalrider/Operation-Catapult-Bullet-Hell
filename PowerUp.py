import pygame, math
from pygame.locals import *
from Bullet import *


class PowerUp(pygame.sprite.Sprite):

    """
        When angle is 0, the enemy is pointing straight down. Then it is -90 to 90 degrees
    """
    def __init__(self, pos, pType):
        super().__init__()
        self.image = pygame.image.load("images\\Shield_PowerUp.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.radius = 17

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)