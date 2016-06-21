import pygame
from pygame.locals import *

class scrollScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("egg.gif")
        self.dx = -5
        self.image.get_rect().bottom = 800
        
    def update(self):
        self.rect().bottom += self.dx
        if self.image.get_rect().bottom >= 1600:
            self.image.get_rect().bottom = 800

class Ship(pygame.sprite.Sprite):

    def __init__ (self):
        global hasBullet
        super().__init__()
        self.image = pygame.image.load("egg.gif")
        #surf.blit(self.image, [0, 0])
        self.image.get_rect().centerx = 250
        self.image.get_rect().centery = 400
        hasBullet = False

    def update(self):
        global hasBullet

        key = pygame.key.get_pressed()
        
        if key[K_w]:
            self.image.get_rect().centery += -3
        if key[K_s]:
            self.image.get_rect().centery += 3
        if key[K_d]:
            self.image.get_rect().centerx += 3
        if key[K_a]:
            self.image.get_rect().centerx += -3
        if key[K_SPACE]:
            bulletGroup.add(Bullet(self.image.get_rect().midtop))
    
        if self.image.get_rect().centerx > 500-5:
            self.image.get_rect().centerx = 500-5
        if self.image.get_rect().centerx < 5:
            self.image.get_rect().centerx = 5
        if self.image.get_rect().centery > 500-5:
            self.image.get_rect().centery = 500-5
        if self.image.get_rect().centery < 5:
            self.image.get_rect().centery = 5

    def draw(self, surf):
        pygame.draw.rect(surf, [255, 000, 000], self.image.get_rect(), 0)

class Bullet(pygame.sprite.Sprite):

    def __init__ (self, surf, pos):
        super().__init__()
        self.image = pygame.image.load("egg.gif")
        self.image.get_rect().center = pos
        #surf.blit(self.image, [x, y])
        
    def update(self, surf):
        if self.image.get_rect().right > 600:
            self.kill()
        else:
            self.image.get_rect().move_ip(15, 0)
            self.draw(surf)

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.image.get_rect(), 0)