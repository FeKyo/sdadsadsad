import pygame as pg

pg.init

# X = blocos - T = traps - P = player - G - Goal
world_map = [
    '                                '#32

]
tile_size = 32

WIDTH, HEIGHT = 640, len(world_map) * tile_size