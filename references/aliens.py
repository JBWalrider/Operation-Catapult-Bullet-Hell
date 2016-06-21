#!/usr/bin/env python
# Load Enemy Objects

from helpers import *

class Alien1(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image('aliens.png', -1)

        screen = pygame.display.get_surface()

        self.area = screen.get_rect()
        self.y = random.randrange(1, 600)

        self.rect.topleft = 800, self.y

        self.move = random.randrange(1, 5)



    def update(self):

        self._move()


    def _move(self):
        newpos = self.rect.move((-self.move, 0))
        if self.rect.right == 0:
            self.y = random.randrange(100, 500)
            self.rect.topleft = 800, self.y
            self.move = random.randrange(1, 5)
            newpos = self.rect.move((-self.move, 0))

        self.rect = newpos
        
class Alien2(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image('aliens2.png', -1)

        screen = pygame.display.get_surface()

        self.area = screen.get_rect()
        self.y = random.randrange(1, 600)

        self.rect.topleft = 800, self.y

        self.move = random.randrange(1, 5)



    def update(self):

        self._move()



    def _move(self):
        newpos = self.rect.move((-self.move, 0))
        if self.rect.right == 0:
            self.y = random.randrange(100, 500)
            self.rect.topleft = 800, self.y
            self.move = random.randrange(1, 5)
            newpos = self.rect.move((-self.move, 0))

        self.rect = newpos
        
class Alien3(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image('aliens3.png', -1)

        screen = pygame.display.get_surface()

        self.area = screen.get_rect()
        self.y = random.randrange(1, 600)

        self.rect.topleft = 800, self.y

        self.move = random.randrange(1, 5)



    def update(self):

        self._move()



    def _move(self):
        newpos = self.rect.move((-self.move, 0))
        if self.rect.right == 0:
            self.y = random.randrange(100, 500)
            self.rect.topleft = 800, self.y
            self.move = random.randrange(1, 5)
            newpos = self.rect.move((-self.move, 0))

        self.rect = newpos