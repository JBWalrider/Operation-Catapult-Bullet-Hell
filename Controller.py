import pygame
from pygame.locals import *
from Ship import *
from Bullet import *
from ScrollScreen import *
from Enemy import *
from random import randint

class Controller:

    SCREEN_WIDTH = None
    SCREEN_HEIGHT = None
    SCREEN_SIZE = None
    
    scroll = None
    ship = None

    spaceGroup = None
    shipGroup = None
    bulletGroup = None
    enemyGroup = None
    

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
        self.enemyGroup.draw(self.screen)

    def shoot(self, b):
        self.bulletGroup.add(b)

    def start(self):
        music = pygame.mixer.music.load("sounds/sound2.mp3")
        pygame.mixer.music.play()

        self.scroll = ScrollScreen(self.SCREEN_HEIGHT)
        self.ship = Ship(self.SCREEN_SIZE, self)

        self.spaceGroup = pygame.sprite.RenderPlain((self.scroll))
        self.shipGroup = pygame.sprite.RenderPlain((self.ship))
        self.bulletGroup = pygame.sprite.RenderPlain(()) 
        self.enemyGroup = pygame.sprite.RenderPlain(())

        pygame.time.set_timer(pygame.USEREVENT+1, 50)                   #Timer for bullet
        pygame.time.set_timer(pygame.USEREVENT+2, 100)                  #Timer for background
        pygame.time.set_timer(pygame.USEREVENT+3, 250)                  #Timer for shooting
        pygame.time.set_timer(pygame.USEREVENT+4, 10)                   #Timer for moving
        pygame.time.set_timer(pygame.USEREVENT+5, 500)    #Timer for Enemy Shooting
        pygame.time.set_timer(pygame.USEREVENT+6, 800)   #Timer for enemy spawn

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
                    self.enemyGroup.update()
                if event.type == USEREVENT+5:
                    enemyList = self.enemyGroup.sprites()
                    for i in range(len(enemyList)):
                        enemyList[i].shoot()
                if event.type == USEREVENT+6:
                    sType = randint(0, 1)
                    #path = "images\\Enemy_" + (1+sType)
                    path = "images\\Enemy_" + str(sType) + ".png"
                    initX = randint(0, 500)
                    initDX = randint(-1, 1)
                    initDY = randint(1, 2)
                    enemy = Enemy(path, initX, 0, initDX, initDY, sType, self)
                    self.enemyGroup.add(enemy)
                  

            pygame.display.update()

            self.repaint()

        pygame.quit()    
