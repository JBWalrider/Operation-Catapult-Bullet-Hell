import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
    drawBullet = False

    def __init__ (self, screenSize):
        super().__init__()
        self.image = pygame.image.load("images\\Spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery = 400
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.offset = 5

    def update(self):
        key = pygame.key.get_pressed()
        
        if key[K_w]:
            self.rect.centery += -3
        if key[K_s]:
            self.rect.centery += 3
        if key[K_d]:
            self.rect.centerx += 3
        if key[K_a]:
            self.rect.centerx += -3
        if key[K_SPACE]:
            self.drawBullet = True
        else:
            self.drawBullet = False
    
        if self.rect.centerx > self.screenWidth-self.offset:
            self.rect.centerx = self.screenWidth-self.offset
        if self.rect.centerx < self.offset:
            self.rect.centerx = self.offset
        if self.rect.centery > self.screenHeight-self.offset:
            self.rect.centery = self.screenHeight-self.offset
        if self.rect.centery < self.offset:
            self.rect.centery = self.offset

    def draw(self, surf):
        pygame.draw.rect(surf, [255, 000, 000], self.rect, 0)