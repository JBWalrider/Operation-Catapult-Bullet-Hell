class Ship():

    def __init__ (self



class Bullet():

    def __init__ (self, pos):
        self.rect = Rect((290, 490), (20, 20)) #change this to a sprite
        self.rect.center = pos
        
    def update(self):
        if self.rect.right > 600:
            self.kill()
        else:
            self.rect.move_ip(15, 0)

    def kill(self):
        pass
        #get rid of the object