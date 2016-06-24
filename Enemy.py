import pygame
from pygame.locals import *
from Enemy_Bullet import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, imagePath, initX, initY, initDX, initDY, sType, controller, imagePath_2):
        super().__init__()
        self.imageList = (pygame.image.load(imagePath), pygame.image.load(imagePath_2))
        self.imageIndex = 0
        self.image = self.imageList[self.imageIndex]
        self.rect = self.image.get_rect()
        self.rect.centerx = initX 
        self.rect.centery = initY
        self.dx = initDX
        self.dy = initDY
        self.sType = sType
        self.controller = controller
        self.radius = 10
       

    def rightOOB(self):
        #print(self.rect.right > 600 + self.rect.height)
        return self.rect.right > 600 + self.rect.height

    def leftOOB(self):
        #print(self.rect.left < -100 - self.rect.height)
        return self.rect.left < -100 - self.rect.height
    def downOOB(self):
        #print(self.rect.bottom > 900 + self.rect.height)
        return self.rect.bottom > 900 + self.rect.height

        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        #print("update")
        if self.rightOOB() or self.leftOOB() or self.downOOB():
            self.kill() 

    def shoot(self):
        if self.sType == 0:     #Single straight down
            eb = Enemy_Bullet(self.rect.center, 12, 0)
            self.controller.shoot(eb)
        elif self.sType == 1:   #Triple shot (small cone)
            for i in range(-1, 2):
                eb = Enemy_Bullet(self.rect.center, 12, i*45)
                self.controller.shoot(eb)
        elif self.sType == 2:   #Six shot (large cone)
            for i in range(-3, 4):
                eb = Enemy_Bullet(self.rect.center, 12, i*15)
                self.controller.shoot(eb)

    def draw(self, surface):
        pygame.draw.rect(surface, [255, 000, 000], self.rect, 0)

    def switchIndex(self, index):
        self.imageIndex = index