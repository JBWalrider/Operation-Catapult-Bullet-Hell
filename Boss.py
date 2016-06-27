import pygame, math
from random import randint
from Enemy_Bullet import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, imageID, c):
        super().__init__()
        img = pygame.image.load("images\\Final_Boss.png")
        self.imageList = [img]
        self.imageIndex = imageID
        self.image = self.imageList[imageID]
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery = -50
        self.health = 100
        self.destY = 150
        self.dx = 1
        self.controller = c
        self.radius = 70

    def spread(self):
        for i in range(-3, 4):
            eb = Enemy_Bullet(self.rect.center, 12, i*15)
            self.controller.shoot(eb)

    def alternatingSpread(self, startAngle):
        for i in range(-3, 3):
            eb = Enemy_Bullet(self.rect.center, 12, startAngle + i*15)
            self.controller.shoot(eb)
    
    def hardShot(self):
        x = math.degrees(math.atan(40/500))
        for i in range(-7, 7):
            eb = Enemy_Bullet(self.rect.center, 12, x + 2*i*x)
            self.controller.shoot(eb)

    def loseHealth(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False

    def shoot(self):
        attack = randint(0, 2)
        if attack == 0:
            self.hardShot()
        elif attack == 1:
            self.spread()
        elif attack == 2:
            self.alternatingSpread(-20)
            self.alternatingSpread(20)
            
    def update(self):
        if self.rect.centery == self.destY:
            if self.rect.right >= 490 or self.rect.left <= 10:
                self.dx *= -1
            
            self.rect.move_ip(self.dx, 0)
        else:
            self.rect.move_ip(0, 1)
    
    def draw(self, surface):
        pygame.draw.rect(surface, [255, 000, 000], self.rect, 0)
    