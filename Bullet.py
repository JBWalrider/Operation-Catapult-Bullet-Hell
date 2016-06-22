import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):

    speed = None

    def __init__ (self, surf, pos):
        super().__init__()
        self.image = pygame.image.load("images\\Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = -15
        
    def update(self):
        if self.rect.top < 0 - self.rect.height:
            self.kill()
        else:
            self.rect.move_ip(0, self.speed)

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)