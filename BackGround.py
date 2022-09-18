import pygame as pg

class  BackGround(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Sprites/bg.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 300)

    def update(self):
        self.rect.topleft = ( self.rect.topleft[0]- 3, self.rect.topleft[1])
        if( abs(self.rect.topleft[0]) >= self.rect.width - 1280):
            self.rect.topleft = ( 0, self.rect.topleft[1])

