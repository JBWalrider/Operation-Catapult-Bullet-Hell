import pygame
from pygame.locals import *

class Enemy_Bullet(pygame.sprite.Sprite):

    speed = None
    straightDown = 0
    fourtyFiveDegrees_1 = 1
    fourtyFiveDegrees_2 = 2


    def __init__ (self, surf, pos, type1):
        super().__init__()
        self.image = pygame.image.load("images\\Enemy_Bullet.png")
        self.rect = self.image.get_rect()
        self.type = type1
        self.rect.center = pos
        self.speed = 15
        
    def update(self):
        if self.rect.top < 0 - self.rect.height or self.rect.right > 500 + self.rect.height or self.rect.left < 0 - self.rect.height or self.rect.bottom > 800 + self.rect.height :
            self.kill() 
        else:
            if self.type == self.straightDown:
                self.rect.move_ip(0, self.speed)
            if self.type == self.fourtyFiveDegrees_1:
                self.rect.move_ip(self.speed, self.speed)
            if self.type == self.fourtyFiveDegrees_2:
                self.rect.move_ip(-self.speed, self.speed)

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)