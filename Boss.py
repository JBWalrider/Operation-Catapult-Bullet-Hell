import randint, math

class Boss:
    def __init__(self, imageID, c):
        #Load images
        #type1 = pygame.image.load("images\\"),
        self.imageList = []
        self.image = self.imageList[imageID]
        self.rect = self.image.get_rect()
        self.health = 200
        self.destY = 200
        self.dx = 2
        self.controller = c

    def spread(self):
        for i in range(-3, 4):
            eb = Enemy_Bullet(self.rect.center, 12, i*15)
            self.controller.shoot(eb)

    def alternatingSpread(self, startAngle):
        for i in range(-3, 3):
            eb = Enemy_Bullet(self.rect.center, 12, startAngle + i*15)
            self.controller.shoot(eb)
    
    def hardShot(self):
        x = math.degrees(math.atan(40/500))
        for i in range(-7, 7):
            eb = Enemy_Bullet(self.rect.center, 12, x + 2*i*x)
            self.controller.shoot(eb)

    def loseHealth(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        else
            return False
            
    def shoot(self):
        attack = randint(0, 2)
        if attack == 0:
            self.alternatingSpread(37.5)
        elif attack == 1:
            self.spread()
        elif attack == 2:
            self.alternatingSpread(45)
        elif attack == 3:
            self.hardShot()
            
    def update(self):
        if self.rect.y == self.destY:
            if self.rect.right >= 450 or self.rect.left <= 50:
                self.dx *= -1
            else:
                self.rect.move_ip(self.dx, 0)
        else:
            self.rect.move_ip(0, 1)

    