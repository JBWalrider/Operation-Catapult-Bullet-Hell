import pygame
from pygame.locals import *

class ScrollScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("egg.gif")
        self.rect = self.image.get_rect()
        self.dx = -5
        self.rect.bottom = 800
        
    def update(self):
        self.rect().bottom += self.dx
        if self.rect.bottom >= 1600:
            self.rect.bottom = 800

class Ship(pygame.sprite.Sprite):

    def __init__ (self):
        global hasBullet
        super().__init__()
        self.image = pygame.image.load("egg.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery = 400
        hasBullet = False

    def update(self):
        global hasBullet, drawBullet

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
            drawBullet = True
        else:
            drawBullet = False
    
        if self.rect.centerx > 500-5:
            self.rect.centerx = 500-5
        if self.rect.centerx < 5:
            self.rect.centerx = 5
        if self.rect.centery > 500-5:
            self.rect.centery = 500-5
        if self.rect.centery < 5:
            self.rect.centery = 5

    def draw(self, surf):
        pygame.draw.rect(surf, [255, 000, 000], self.rect, 0)

class Bullet(pygame.sprite.Sprite):

    def __init__ (self, surf, pos):
        super().__init__()
        self.image = pygame.image.load("testSprite.gif")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:
            self.rect.move_ip(0, -15)

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)

def main():    

    global ship, bullet, drawBullet
    
    drawBullet = False

    pygame.init()

    screen = pygame.display.set_mode((500, 800))

    pygame.display.set_caption("Bullet Hell")

    pygame.mouse.set_visible(0)

    scroll = ScrollScreen()
    global ship
    ship = Ship()

    spaceGroup = pygame.sprite.RenderPlain((scroll))
    global shipGroup
    shipGroup = pygame.sprite.RenderPlain((ship))
    global bulletGroup
    bulletGroup = pygame.sprite.RenderPlain(())  

    pygame.key.set_repeat(1000000)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        shipGroup.update()
        bulletGroup.update()
        pygame.display.update()
        
        if drawBullet == True:
            bulletGroup.add(Bullet(screen, ship.rect.midtop))

        screen.fill((0, 0, 0))
        
        
        spaceGroup.draw(screen)
        shipGroup.draw(screen)
        bulletGroup.draw(screen)

    pygame.quit()

if __name__ == '__main__':

    main()