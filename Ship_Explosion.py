class Ship_Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("shipExplosion.png")
        self.rect.center = pos
        
    def update(self):
        #implement timer, have self.kill() after 1-2 seconds
            exit() #if player dies, game over. Go to aftergame (play again, quit)