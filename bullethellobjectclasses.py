import pygame, time, random
from pygame.locals import *
from threading import Thread


pygame.init()
screen = pygame.display.set_mode([500,800])
pygame.display.set_caption("My Window")
pygame.key.set_repeat(50, 1000)

class MyThread(Thread):
    def __init__(self, b, xc, yc, screen):
        ''' Constructor. '''
 
        Thread.__init__(self)
        self.bullet = b
        self.xc = xc
        self.yc = yc
        self.screen = screen

 
 
    def run(self):
        for i in range(1, 800):
            self.bullet.shoot(self.screen, self.xc, self.yc)
            self.yc -=1
 
            # Sleep for random time between 1 ~ 3 second
            secondsToSleep = 0.001
            time.sleep(secondsToSleep)
            pygame.display.flip()



class Ship(pygame.sprite.Sprite):

    def __init__ (self, pos, screen):
        super().__init__()
        self.image = pygame.image.load('Main_Character.png')
        screen.blit(self.image, pos)


class Bullet(pygame.sprite.Sprite):

    def __init__ (self, pos, angle, screen):
        super().__init__()
        self.image = pygame.image.load('Bullet.png')
        screen.blit(self.image, pos)

    def shoot(self, screen, xc, yc):
        xcoord = xc
        ycoord = yc
        ycoord -= 1
        self.image.get_rect().move(xcoord, ycoord)
        screen.blit(self.image, [xcoord, ycoord])
            
            
            
        
           
        
        # while self.image.get_rect().y < 900:
        #self.image.get_rect().y -= 100
            
        
        
    def update(self):
        if self.rect.right > 600:
            self.kill()
        else:
            self.rect.move_ip(15, 0)

    def kill(self):
        pass
        #get rid of the object



def test():
   
    center = [250,780]
    radius = 50
    drawCircle = True
    drawBullet = False

    
    while True:
        drawBullet = False
        events = pygame.event.get()
        k = pygame.key.get_pressed()
        if k[K_p]:
            t = center
            xc = t[0] + 15
            yc = t[1] - 10
            np = [xc, yc]
            b = Bullet(np, 0, screen)
            myThread1 = MyThread(b, xc, yc, screen)
            myThread1.start()
            drawBullet = True 
        for event in events:
            if event.type == QUIT:
                return
            if event.type == MOUSEMOTION:
                center = event.pos
            else:
                pass
                 
                    


            
            screen.fill((0,0,0))
            
            Ship(center, screen)
            
            pygame.display.flip()
           
            



test()