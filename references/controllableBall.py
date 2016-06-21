import pygame
from pygame.locals import *
import bullet

pygame.init()

x = 200
y = 130
radius = 50
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Bullethell")
pygame.key.set_repeat(10)
screen.fill((0,0,0))

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[K_SPACE]:
        bulletN = bullet(x, y)

    if keys[K_a]:
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, [150, 210, 235], [x, y], radius)
        x -= 1

    if keys[K_d]:
        x += 1
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, [150, 210, 235], [x, y], radius)

    if keys[K_w]:
        y -= 1
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, [150, 210, 235], [x, y], radius)
        
    if keys[K_s]:
        y += 1
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, [150, 210, 235], [x, y], radius)
    
    if x > 600-radius:
        x = 600-radius

    if x < radius:
        x = radius

    if y > 600-radius:
        y = 600-radius

    if y < radius:
        y = radius

    
    pygame.display.update()

pygame.quit()
