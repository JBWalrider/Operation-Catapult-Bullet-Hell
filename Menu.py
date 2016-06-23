<<<<<<< HEAD
import pygame
from pygame.locals import *
from Controller import *

c = Controller(500, 700)

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        c.screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
menu_font = pygame.font.Font(None, 40)
options = [Option("START", (200, 540)),Option("CREDITS", (182, 580))]

def menustart():
    while True:
        pygame.event.pump()
        pygame.mouse.set_visible(1)
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if options[0].hovered == True:
                if event.type == MOUSEBUTTONDOWN:
                    pygame.mouse.set_visible(0)
                    c.start()
                    return
                
                

TitleScreen = pygame.image.load("images/Title.png")
TitleScreen.convert()
c.screen.blit(TitleScreen, (0,0))

menustart()
=======
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Catabullet")
window.geometry("500x800")
window.wm_iconbitmap('images\\SpaceshipIcon.ico')

startb = ttk.Button(window)
startb.pack()

window.mainloop() 
>>>>>>> Timer
