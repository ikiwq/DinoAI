import pygame as pg

class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, sprite, type = 0, speed= 3):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.rectarray = []

        if(type==0):
            self.rectarray.append( pg.rect.Rect((x+10,y), (20, 96)))
            self.rectarray.append(pg.rect.Rect((x+42, y+40), (42, 96)))
        if( type==1 ):
            self.rectarray.append(pg.rect.Rect((x+5, y+40), (27, 45)))
            self.rectarray.append(pg.rect.Rect((x + 37, y), (42, 96)))
        self.speed = speed

    def update(self):
        self.rect.topleft = (self.rect.topleft[0] - self.speed, self.rect.topleft[1])
        for rect in self.rectarray:
            rect.x -= self.speed

