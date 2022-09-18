import pygame as pg

class Dino(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loadSprites()
        self.image = self.walkArray[0]
        self.rect = self.image.get_rect()
        self.y = 330
        self.x = 150
        self.rect.topleft = (self.x, self.y)
        self.rect.w = self.rect.w/1.3
        self.mask = pg.mask.from_surface(self.image)


        self.score = 0

        self.frame = 0
        self.tickCounter = 0

        self.VelY = 0
        self.Grav = 0.2

        self.canJump = True
        self.falling = False

        self.isDead = False

    def loadSprites(self):
        #loading all the sprites into a single array, then loop through it to animate
        self.walkArray = []
        for i in range(0, 4):
            self.walkArray.append(pg.image.load( "Sprites/Dino/"+ str(i+1) + "-" + str(i+1) + ".png"))

    def jump(self):
        self.VelY = -10
        self.canJump = False
        self.falling = True

    def update(self):
        if(self.isDead):
            self.image = self.walkArray[3]
            return

        self.score += 0.1

        if(self.falling):
            self.VelY += self.Grav

        if(self.rect.topleft[1] > 330 - self.VelY):
            self.VelY = 0
            self.rect.topleft = (self.rect.topleft[0], 330)
            self.falling = False
            self.canJump = True


        self.y += self.VelY
        self.rect.topleft = (self.rect.topleft[0], self.y)

        #animation
        self.tickCounter += 1
        if self.tickCounter > 10:
            if self.frame < 2:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.walkArray[self.frame]

            self.tickCounter = 0