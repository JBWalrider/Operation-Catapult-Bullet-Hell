import pygame, math
from pygame.locals import *
from Bullet import *

class Enemy_Bullet(Bullet):

    def __init__(self, pos, speed, angle): #When angle is 0, the enemy is pointing straight down. Then it is -90 to 90 degrees
        super().__init__(pos)
        self.image = pygame.image.load("images\\Enemy_Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.angle = math.radians(angle)
        self.radius = 4
        self.team = 1

    def upOOB(self):
        return self.rect.top < 0 - self.rect.height
    def rightOOB(self):
        return self.rect.right > 500 + self.rect.height
    def leftOOB(self):
        return self.rect.left < 0 - self.rect.height
    def downOOB(self):
        return self.rect.bottom > 800 + self.rect.height

    def update(self):
        if self.upOOB() or self.rightOOB() or self.leftOOB() or self.downOOB():
            self.kill() 
        else:
            self.rect.move_ip(math.copysign(math.sin(self.angle) * self.speed, self.angle), math.fabs(math.cos(self.angle) * self.speed))

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)

