#!/usr/bin/env python
import pygame
from pygame.locals import *

class Player():

    def __init__(self):

        self.rect = Rect((280, 480), (40, 40))
        self.x_dist = 5
        self.y_dist = 5
        self.lasertimer = 0
        self.lasermax = 5
        self.rect.centery = 400
        self.rect.centerx = 50
        
    def update(self):
        key = pygame.key.get_pressed()
        
        # Movement
        if key[K_UP]:
            self.rect.centery += -3
        if key[K_DOWN]:
            self.rect.centery += 3
        if key[K_RIGHT]:
            self.rect.centerx += 3
        if key[K_LEFT]:
            self.rect.centerx += -3
        
        # Lasers
        if key[K_SPACE]:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                #laserSprites.add(Laser(self.rect.midtop))
                self.lasertimer = 0
       
        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 600)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, 800)
        self.rect.left = max(self.rect.left, 0)
                                                     
class Laser():
    def __init__(self, pos):
        self.rect = Rect((290, 490), (20, 20))
        self.rect.center = pos
    
    def update(self):
        global count
        if count < 41:
            self.rect.move_ip(15, 0)
        else:
            count = 0
                                                                                                              
def main():    
# Initialize Everything

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Space Quest')

    pygame.mouse.set_visible(0)



# Create The Backgound

    background = pygame.Surface(screen.get_size())

    background = background.convert()

    background.fill((255, 000, 000))



# Display The Background

    screen.blit(background, (0, 0))

    pygame.display.flip()
        
# Initialize Game Objects
    global clock

    clock = pygame.time.Clock()
    global player

    player = Player()
    laser = Laser(player.rect.midtop)



# Main Loop
    global count
    count = 0
    going = True

    while going:

        clock.tick(60)



        # Input Events

        for event in pygame.event.get():

            if event.type == QUIT:

                going = False

            elif event.type == KEYDOWN and event.key == K_ESCAPE:

                going = False

        # Update
        player.update()
        laser.update()
        #laserSprites.update()



        screen.blit(background, (0, 0))


        # Draw
        
        #playerSprite.draw(screen)
        #laserSprites.draw(screen)
        #player.draw(screen)
        #laser.draw(screen)
        pygame.display.flip()



    pygame.quit()



if __name__ == '__main__':

    main()