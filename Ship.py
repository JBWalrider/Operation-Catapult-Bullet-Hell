import pygame
from pygame.locals import *
from Bullet import *
from Enemy_Bullet import *

class Ship(pygame.sprite.Sprite):
    canShoot = False
    drawBullet = False

    def __init__ (self, screenSize, controller):
        super().__init__()
        self.image = pygame.image.load("images\\Spaceship.png")
        self.rect = self.image.get_rect()
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1]
        self.rect.centerx = self.screenWidth / 2
        self.rect.centery = self.screenHeight / 2
        self.offset = self.rect.width/2
        self.controller = controller
        self.radius = 12
        self.lives = 3
        self.invincible = False
        self.invincTime = 0
   
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
                b = Bullet( self.rect.midtop)
                self.controller.shoot(b)
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
