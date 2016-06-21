import math, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("CataBullet")

TiR=Rect((50,700),(400,200))
SbR=Rect((100,400),(300,150))
Title = pygame.draw.Rect(screen, [255,0,0], TiR, width=0)
StartButton = pygame.draw.Rect(screen, [255,0,0], SbR, width=0)