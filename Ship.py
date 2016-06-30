import pygame, time
from pygame.locals import *
from Bullet import *
from Enemy_Bullet import *

class Ship(pygame.sprite.Sprite):
    canShoot = False
    drawBullet = False

    def __init__ (self, screenSize, controller):
        super().__init__()
        self.imageList = (pygame.image.load("images\\Spaceship.png"), pygame.image.load("images\\Spaceship_Shield.png"), pygame.image.load("images\\Spaceship_ShieldPowerUp.png"))
        self.imageIndex = 0
        self.image = self.imageList[self.imageIndex]
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
        self.shotNumber = 1 #how many shots it can shoot (for trishot powerup)
   
    def update(self):        
        key = pygame.key.get_pressed()
        if key[K_w] or key[K_UP]:
            self.rect.centery += -2
        if key[K_s] or key[K_DOWN]:
            self.rect.centery += 2
        if key[K_d] or key[K_RIGHT]:
            self.rect.centerx += 2
        if key[K_a] or key[K_LEFT]:
            self.rect.centerx += -2
        if key[K_SPACE]:
            if self.canShoot:
                if self.shotNumber == 1:
                    b = Bullet( self.rect.midtop)
                    self.controller.shoot(b)
                    self.canShoot = False
                if self.shotNumber == 3:
                    b1 = Bullet(self.rect.topleft)
                    b2 = Bullet(self.rect.midtop)
                    b3 = Bullet(self.rect.topright)
                    self.controller.shoot(b1)
                    self.controller.shoot(b2)
                    self.controller.shoot(b3)
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

    def switchIndex(self, index): #switch between regular and shield sprites
        self.imageIndex = index
        self.image = self.imageList[self.imageIndex]

    def giveShield(self, duration, shType): #shield type
        self.invincTime =  time.time()
        self.invincible = True
        self.duration = duration
        self.switchIndex(shType)

    def loseLife(self):
        self.lives -= 1
    
    def addLife(self):
        self.lives = 3

    def changeShotTri(self, duration):
        self.triShotTime = time.time()
        self.shotNumber = 3
        self.duration1 = duration
        #duration1 is for powerups, duration is for invincibility period

    def changeShotSingle(self):
        self.shotNumber = 1

