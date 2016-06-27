import pygame, time
from pygame.locals import *
from Ship import *
from Bullet import *
from ScrollScreen import *
from Enemy import *
from random import randint
import MainMenu
import PauseMenu
from PowerUp import *

class Controller:

    SCREEN_WIDTH = None
    SCREEN_HEIGHT = None
    SCREEN_SIZE = None
    
    scroll = None
    ship = None

    spaceGroup = None
    powerUpGroup = None
    shipGroup = None
    bulletGroup = None
    enemyGroup = None
    

    def __init__(self, w, h):
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.diff = 0
        


        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        pygame.display.set_caption("Bullet Hell")
        pygame.mouse.set_visible(0)
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        
    def repaint(self):
        self.screen.fill((0, 0, 0))
        self.spaceGroup.draw(self.screen)
        self.powerUpGroup.draw(self.screen)
        self.shipGroup.draw(self.screen)
        self.bulletGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)
             
    def shoot(self, b):
        self.bulletGroup.add(b)
    
    def setdiff(self,diff):
        self.diff = diff

    def start(self):    
        global pause 
        pause = False
        multiplier = 1
        sc = 0

        pygame.mixer.music.load("sounds/gameMusic.mp3")
        pygame.mixer.music.play(-1) 

        self.scroll = ScrollScreen(self.SCREEN_HEIGHT)
        self.ship = Ship(self.SCREEN_SIZE, self)

        self.spaceGroup = pygame.sprite.RenderPlain((self.scroll))
        self.shipGroup = pygame.sprite.RenderPlain((self.ship))
        self.bulletGroup = pygame.sprite.RenderPlain(()) 
        self.enemyGroup = pygame.sprite.RenderPlain(())
        self.powerUpGroup = pygame.sprite.RenderPlain(())

        enemyDeath = pygame.mixer.Sound("sounds/enemyDeath.wav")
        shipShieldDeath = pygame.mixer.Sound("sounds/shipShieldDeath.wav")
        shipDeath = pygame.mixer.Sound("sounds/shipDeath.wav")
        shipPowerUp = pygame.mixer.Sound("sounds/shipPowerUp.wav")
        bossFight = pygame.mixer.Sound("sounds/bossFight.wav")

        scoreFont = pygame.font.Font(None, 40)    

        pygame.time.set_timer(pygame.USEREVENT+1, 50)                   #Timer for bullet
        pygame.time.set_timer(pygame.USEREVENT+2, 100)                  #Timer for background
        pygame.time.set_timer(pygame.USEREVENT+3, 300)                  #Timer for shooting
        pygame.time.set_timer(pygame.USEREVENT+4, 10)                   #Timer for moving
        pygame.time.set_timer(pygame.USEREVENT+5, self.diff)            #Timer for Enemy Shooting
        pygame.time.set_timer(pygame.USEREVENT+6, self.diff)            #Timer for enemy spawn
        pygame.time.set_timer(pygame.USEREVENT+7, 20000)                #Timer for Power Up spawn
        pygame.time.set_timer(pygame.USEREVENT, 120000)                 #Timer for boss spawn


        while True:
            scRendered = scoreFont.render(str(sc), True, (150, 150, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "Quit"
                if event.type == USEREVENT+1:
                    bulletList = self.bulletGroup.sprites()   
                    self.bulletGroup.update()
                    enemyList = self.enemyGroup.sprites()
                    for x in range(len(bulletList)):
                        for i in range(len(enemyList)):
                            if bulletList[x].team == 0 and pygame.sprite.collide_circle(bulletList[x], enemyList[i]):
                                enemyDeath.play()
                                sc += 50*multiplier
                                multiplier += 1
                                enemyList[i].kill()
                                bulletList[x].kill()
                        if bulletList[x].team == 1 and pygame.sprite.collide_circle(self.ship, bulletList[x]):
                            bulletList[x].kill()
                            if not self.ship.invincible:
                                if self.ship.lives == 1:
                                    shipDeath.play()
                                else:
                                    shipShieldDeath.play()
                                self.ship.lives -= 1
                                multiplier = 1
                                self.ship.giveShield(2, 1)
                           
                            if self.ship.lives <= 0:
                                time.sleep(1)
                                return "Exit"
                            
                if event.type == USEREVENT+2:
                    self.spaceGroup.update()
                if event.type == USEREVENT+3:
                    self.ship.canShoot = True
                if event.type == USEREVENT+4:
                    powerUp = self.powerUpGroup.sprites()
                    for x in range(len(self.powerUpGroup)):
                        if pygame.sprite.collide_circle(self.ship, powerUp[x]):
                            powerUp[x].power(self.ship)
                            powerUp[x].kill()
                            shipPowerUp.play()
                    
                    self.shipGroup.update()
                    self.enemyGroup.update()
                if event.type == USEREVENT+5:
                    enemyList = self.enemyGroup.sprites()
                    for i in range(len(enemyList)):
                        enemyList[i].shoot()
                if event.type == USEREVENT+6:
                    sType = randint(0, 1)
                    path = "images\\Enemy_" + str(sType) + ".png"
                    initX = randint(100, 400)
                    initDX = randint(-1, 1)
                    initDY = randint(1, 1)
                    enemy = Enemy(path, initX, 0, initDX, initDY, sType, self, "images\\Enemy_1.png")
                    self.enemyGroup.add(enemy)
                if event.type == USEREVENT+7:
                    xcoord = randint(100, 400)
                    ycoord = randint(100, 450)
                    pType = randint(0, 2)
                    pUp = PowerUp((xcoord, ycoord), pType)
                    self.powerUpGroup.add(pUp)
                if event.type == USEREVENT:
                    pass
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    pauseMenu = PauseMenu.Menu(self)
                    action = pauseMenu.pause(self)
                    if action != "Continue":
                        return action

            if self.ship.invincible and time.time() - self.ship.invincTime >= self.ship.duration:
                self.ship.switchIndex(0)
                self.ship.invincible = False
            if self.ship.shotNumber == 3 and time.time() - self.ship.triShotTime >= self.ship.duration1:
                self.ship.changeShotSingle()
                
            pygame.display.update()

            self.repaint()
            self.screen.blit(scRendered, (500-scRendered.get_rect().right-2, 2))
