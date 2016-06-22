import pygame
from pygame.locals import *
from Ship import *
from Bullet import *
from ScrollScreen import *

class Controller:

    SCREEN_WIDTH = None
    SCREEN_HEIGHT = None
    SCREEN_SIZE = None
    
    scroll = None
    ship = None

    spaceGroup = None
    shipGroup = None
    bulletGroup = None
    

    def __init__(self, w, h):
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        
        pygame.display.set_caption("Bullet Hell")
        pygame.mouse.set_visible(0)
        pygame.init()

    def repaint(self):
        self.screen.fill((0, 0, 0))
        self.spaceGroup.draw(self.screen)
        self.shipGroup.draw(self.screen)
        self.bulletGroup.draw(self.screen)

    def start(self):        
        self.scroll = ScrollScreen()
        self.ship = Ship(self.SCREEN_SIZE)

        self.spaceGroup = pygame.sprite.RenderPlain((self.scroll))
        self.shipGroup = pygame.sprite.RenderPlain((self.ship))
        self.bulletGroup = pygame.sprite.RenderPlain(()) 

        pygame.time.set_timer(pygame.USEREVENT+1, 50)       #Timer for bullet
        pygame.time.set_timer(pygame.USEREVENT+2, 250)      #Timer for background
        pygame.time.set_timer(pygame.USEREVENT+3, 250)      #Timer for shooting
        pygame.time.set_timer(pygame.USEREVENT+4, 10)      #Timer for moving

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == USEREVENT+1:
                    self.bulletGroup.update()
                if event.type == USEREVENT+2:
                    self.spaceGroup.update()
                if event.type == USEREVENT+3:
                    self.ship.canShoot = True
                if event.type == USEREVENT+4:
                    self.shipGroup.update()

            pygame.display.update()
            
            if self.ship.drawBullet:
                self.bulletGroup.add(Bullet(self.screen, self.ship.rect.midtop))
                self.ship.drawBullet = False

            self.repaint()

        pygame.quit()

    