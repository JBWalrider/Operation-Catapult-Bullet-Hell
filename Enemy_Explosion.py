class Enemy_Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("enemyExplosion.png")
        self.rect.center = pos

    def update(self):
        #implement timer, have self.kill() after 1-2 seconds


"""
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("enemyexplosion.png", -1)
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10
        
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            exit()
"""