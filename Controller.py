import pygame, time, os
from pygame.locals import *
from Ship import *
from Bullet import *
from ScrollScreen import *
from Enemy import *
from random import randint
import MainMenu
import PauseMenu
from ezText import eztext
from PowerUp import *
from Boss import *

class Controller(pygame.sprite.Sprite):

    SCREEN_WIDTH = None
    SCREEN_HEIGHT = None
    SCREEN_SIZE = None
    
    spaceGroup = None
    powerUpGroup = None
    shipGroup = None
    bulletGroup = None
    enemyGroup = None
    bossGroup = None
    
    def __init__(self, w, h):
        super().__init__()
        self.heartList = (pygame.image.load("images\\Heart_1.png"), pygame.image.load("images\\Heart_2.png"), pygame.image.load("images\\Heart_3.png"))
        self.heartImage = self.heartList[2]
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
        self.bossGroup.draw(self.screen)
        self.screen.blit(self.heartImage, (0,0))
        self.shipGroup.draw(self.screen)
        self.bulletGroup.draw(self.screen)
        self.enemyGroup.draw(self.screen)

    def shoot(self, b):
        self.bulletGroup.add(b)
    
    def setdiff(self,diff):
        self.diff = diff

    def start(self):    
        global pause
        count = 0
        pause = False
        multiplier = 1
        gCount = 0 #easter egg
        sc = 0 #score
        pygame.mixer.stop() #stop menu music
        pygame.mixer.music.load("sounds/gameMusic.mp3")
        pygame.mixer.music.play(-1) #plat game music

        self.scroll = ScrollScreen(self.SCREEN_HEIGHT)
        self.ship = Ship(self.SCREEN_SIZE, self)

        self.spaceGroup = pygame.sprite.RenderPlain((self.scroll))
        self.shipGroup = pygame.sprite.RenderPlain((self.ship))
        self.bulletGroup = pygame.sprite.RenderPlain(()) 
        self.enemyGroup = pygame.sprite.RenderPlain(())
        self.powerUpGroup = pygame.sprite.RenderPlain(())
        self.bossGroup = pygame.sprite.RenderPlain(())

        enemyDeath = pygame.mixer.Sound("sounds\\enemyDeath.wav")
        shipShieldDeath = pygame.mixer.Sound("sounds\\shipShieldDeath.wav")
        shipDeath = pygame.mixer.Sound("sounds\\shipDeath.wav")
        shipPowerUp = pygame.mixer.Sound("sounds\\shipPowerUp.wav")
        bossFight = pygame.mixer.Sound("sounds\\bossFight.wav")

        scoreFont = pygame.font.Font(None, 40)    

        pygame.time.set_timer(pygame.USEREVENT+1, 50)                   #Timer for bullet
        pygame.time.set_timer(pygame.USEREVENT+2, 100)                  #Timer for background
        pygame.time.set_timer(pygame.USEREVENT+3, 300)                  #Timer for shooting
        pygame.time.set_timer(pygame.USEREVENT+4, 10)                   #Timer for moving
        pygame.time.set_timer(pygame.USEREVENT+5, self.diff)            #Timer for enemy Shooting
        pygame.time.set_timer(pygame.USEREVENT+6, self.diff)            #Timer for enemy spawn
        pygame.time.set_timer(pygame.USEREVENT+7, 20000)                #Timer for Power Up spawn
        pygame.time.set_timer(pygame.USEREVENT, 60000)                 #Timer for boss spawn
       
        while True:
            heartNumber = self.ship.lives - 1
            self.heartImage = self.heartList[heartNumber]
            scRendered = scoreFont.render(str(sc), True, (150, 150, 255))
            mtRendered = scoreFont.render("X" + str(multiplier), True, (150, 150, 255))

            for event in pygame.event.get():

                if event.type == QUIT:
                    return "Quit"

                if event.type == USEREVENT+1:
                    bulletList = self.bulletGroup.sprites()   
                    self.bulletGroup.update()
                    enemyList = self.enemyGroup.sprites()
                    bossList = self.bossGroup.sprites()
                    for x in range(len(bulletList)):
                        if bulletList[x].team == 0:
                            for boss in bossList:
                                if pygame.sprite.collide_circle(bulletList[x], boss):
                                    bulletList[x].kill()
                                    if boss.loseHealth(1):
                                        sc += 500*multiplier
                                        boss.kill()
                                        pygame.time.set_timer(pygame.USEREVENT+6, self.diff)
                                        pygame.time.set_timer(pygame.USEREVENT, 60000)

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

                                self.ship.loseLife()
                                heartNumber -= 1
                                multiplier = 1
                                self.ship.giveShield(2, 1)

                            if self.ship.lives <= 0:
                                pygame.time.set_timer(pygame.USEREVENT+1, 0)                   #Timer for bullet
                                pygame.time.set_timer(pygame.USEREVENT+2, 0)                  #Timer for background
                                pygame.time.set_timer(pygame.USEREVENT+3, 0)                  #Timer for shooting
                                pygame.time.set_timer(pygame.USEREVENT+4, 0)                   #Timer for moving
                                pygame.time.set_timer(pygame.USEREVENT+5, 0)                  #Timer for Enemy Shooting
                                pygame.time.set_timer(pygame.USEREVENT+6, 0)                  #Timer for enemy spawn
                                pygame.time.set_timer(pygame.USEREVENT+7, 0)                #Timer for Power Up spawn
                                pygame.time.set_timer(pygame.USEREVENT, 0)                 #Timer for boss spawn
                                txtbx = eztext.Input(maxlength=25, color=(0,0,0), prompt='Enter name: ')
                                while True:
                                    events = pygame.event.get()
                                    # process other events
                                    for event in events:
                                        # close if x button is pressed
                                        if event.type == QUIT: 
                                            return "Exit"

                                    # clear the screen
                                    self.screen.fill((255,255,255))
                                    # update txtbx
                                    s = txtbx.update(events)
                                    if s != None:
                                        string = str(sc) + "\t" + s + "\n"
                                        if self.diff == 1000:
                                            inputPath = "outputs\\Easy.txt"
                                            outputPath = "outputs\\Easy_New.txt"
                                            File = open(inputPath, 'r')
                                            outputFile = open(outputPath, "w")
                                            inserted = False
                                            for line in File:
                                                if not inserted:
                                                    for i in range(len(line)):
                                                        if line[i] == "\t":
                                                            value = int(line[:i])
                                                            if value < sc:
                                                                outputFile.write(string)
                                                                inserted = True
                                                outputFile.write(line)
                                            File.close()
                                            outputFile.close()
                                            os.remove(inputPath)
                                            os.rename(outputPath, inputPath)

                                        elif self.diff == 750:
                                            inputPath = "outputs\\Medium.txt"
                                            outputPath = "outputs\\Medium_New.txt"
                                            File = open(inputPath, 'r')
                                            outputFile = open(outputPath, "w")
                                            inserted = False
                                            for line in File:
                                                if not inserted:
                                                    for i in range(len(line)):
                                                        if line[i] == "\t":
                                                            value = int(line[:i])
                                                            if value < sc:
                                                                outputFile.write(string)
                                                                inserted = True
                                                outputFile.write(line)
                                            File.close()
                                            outputFile.close()
                                            os.remove(inputPath)
                                            os.rename(outputPath, inputPath)

                                        elif self.diff == 500:
                                            inputPath = "outputs\\Hard.txt"
                                            outputPath = "outputs\\Hard_New.txt"
                                            File = open(inputPath, 'r')
                                            outputFile = open(outputPath, "w")
                                            inserted = False
                                            for line in File:
                                                if not inserted:
                                                    for i in range(len(line)):
                                                        if line[i] == "\t":
                                                            value = int(line[:i])
                                                            if value < sc:
                                                                outputFile.write(string)
                                                                inserted = True
                                                outputFile.write(line)
                                            File.close()
                                            outputFile.close()
                                            os.remove(inputPath)
                                            os.rename(outputPath, inputPath)
                                        break
                                    # blit txtbx on the sceen
                                    txtbx.draw(self.screen)
                                    # refresh the display
                                    pygame.display.flip()
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
                    self.bossGroup.update()

                if event.type == USEREVENT+5:
                    enemyList = self.enemyGroup.sprites()
                    for i in range(len(enemyList)):
                        enemyList[i].shoot()
                    bossList = self.bossGroup.sprites()
                    for boss in bossList:
                        boss.shoot()

                if event.type == USEREVENT+6:
                    sType = randint(0, 1)
                    path = "images\\Enemy_" + str(sType) + ".png"
                    initX = randint(100, 400)
                    initDX = randint(-1, 1)
                    initDY = randint(1, 1)
                    enemy = Enemy(path, initX, 0, initDX, initDY, sType, self)
                    self.enemyGroup.add(enemy)

                if event.type == USEREVENT+7:
                    xcoord = randint(100, 400)
                    ycoord = randint(100, 450)
                    pType = randint(0, 2)
                    pUp = PowerUp((xcoord, ycoord), pType)
                    self.powerUpGroup.add(pUp)

                if event.type == USEREVENT:
                    boss = Boss(0, self)
                    self.bossGroup.add(boss)
                    pygame.time.set_timer(pygame.USEREVENT+6, 0)
                    pygame.time.set_timer(pygame.USEREVENT, 0)

                if event.type == KEYDOWN:
                    if event.key == K_w and gCount == 0:
                        gCount = 1
                    if event.key == K_a and gCount == 1:
                        gCount = 2
                    if event.key == K_l and gCount == 2:
                        gCount = 3
                    if event.key == K_r and gCount == 3:
                        gCount = 4
                    if event.key == K_i and gCount == 4:
                        gCount = 5
                    if event.key == K_d and gCount == 5:
                        gCount = 6
                    if event.key == K_e and gCount == 6:
                        gCount = 7
                    if event.key == K_r and gCount == 7:
                        sc = 999999999999999
                        gCount = 8

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
            self.screen.blit(scRendered, (500-scRendered.get_rect().right-2, 2)) #score
            self.screen.blit(mtRendered, (500-mtRendered.get_rect().right-2, 28)) #multiplier

