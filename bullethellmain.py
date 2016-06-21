import pygame
from pygame.locals import *
import bullethellobjectclasses
from bullethellobjectclasses import *

def main():    

    global player, laser

    pygame.init()

    screen = pygame.display.set_mode((500, 800))

    pygame.display.set_caption('Space Quest')

    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
 
    background = background.convert()

    background.fill((000, 000, 000))

    screen.blit(background, (0, 0))

    pygame.display.flip()

    scroll = scrollScreen()
    global player
    ship = Ship()

    spaceGroup = pygame.sprite.RenderPlain((scroll))
    global shipGroup
    shipGroup = pygame.sprite.RenderPlain((ship))
    global bulletGroup
    bulletGroup = pygame.sprite.RenderPlain(())  

    

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        shipr.update()
        
        screen.blit(background, (0, 0))
        
        ship.draw(screen)

if __name__ == '__main__':

    main()