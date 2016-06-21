import pygame
from pygame.locals import *
from Ship import *
from Bullet import *
from ScrollScreen import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

def main():    
    
    drawBullet = False

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.display.set_caption("Bullet Hell")

    pygame.mouse.set_visible(0)

    scroll = ScrollScreen()
    ship = Ship(SCREEN_SIZE)

    spaceGroup = pygame.sprite.RenderPlain((scroll))
    shipGroup = pygame.sprite.RenderPlain((ship))
    bulletGroup = pygame.sprite.RenderPlain(())  

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        shipGroup.update()
        bulletGroup.update()
        spaceGroup.update()
        pygame.display.update()
        
        if ship.drawBullet == True:
            bulletGroup.add(Bullet(screen, ship.rect.midtop))

        screen.fill((0, 0, 0))
        
        
        spaceGroup.draw(screen)
        shipGroup.draw(screen)
        bulletGroup.draw(screen)

    pygame.quit()

if __name__ == '__main__':

    main()