import randint

class Boss:
    def __init__(self, imageID):
        #Load images
        #type1 = pygame.image.load("images\\"),
        self.imageList = []
        self.image = self.imageList[imageID]
        self.rect = self.image.get_rect()
        self.health = 200

    def fan(self):




    def update(self):
        attack = randint(0, 5)
        if attack == 0:
            pass
        elif attack == 1:
            self.spread()
        elif attack == 2:
            self.randomSpread()

    