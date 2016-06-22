import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
    canShoot = False
    drawBullet = False

    def __init__ (self, screenSize):
        super().__init__()
        self.image = pygame.image.load("images\\Spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery = 400
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.offset = self.rect.width/2

   
    def update(self):        
        key = pygame.key.get_pressed()
        
        if key[K_w]:
            self.rect.centery += -2
        if key[K_s]:
            self.rect.centery += 2
        if key[K_d]:
            self.rect.centerx += 2
        if key[K_a]:
            self.rect.centerx += -2
        if key[K_SPACE]:
            if self.canShoot:
                self.drawBullet = True
                self.canShoot = False
    
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
