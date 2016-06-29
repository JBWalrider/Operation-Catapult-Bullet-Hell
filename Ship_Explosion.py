class Ship_Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("shipExplosion.png")
        self.rect.center = pos
        
    def update(self):
        time.sleep(1)    
            exit()