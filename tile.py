import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        img_path = 'Assets/terra.png'
        self.image = pg.image.load(img_path)
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = self.image.get_recct(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift