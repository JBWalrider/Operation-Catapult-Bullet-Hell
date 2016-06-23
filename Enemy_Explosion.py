class Enemy_Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("enemyExplosion.png")
        self.rect.center = pos
        
    def update(self):
        #implement timer, have self.kill() after 1-2 seconds