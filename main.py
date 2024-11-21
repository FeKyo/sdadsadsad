import pygame as pg
import sys
from settings import*
from world import World

pg.init()

screen = pg.display.set_modes((WIDTH, HEIGHT))
pg.display.set_caption("Platformer")

class Platformer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.clock = pg.time.Clock
        self.player_event = False
        self.bg_img = pg.image.load('Assets/Background')
        self.bg_img = pg.transform.scale(self.bg_img, (width, height))

    def main(self):
        world = World(world_map, self.screen)
        while True:
            self.screen.blit(self.bg_img, (0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.QUIT()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.player_event = 'left'
                    if event.key == pg.K_RIGHT:
                        self.player_event = 'right'
                    if event.key == pg.K_SPACE:
                        self.player_event = 'space'
                elif event.type == pg.KEYUP:
                    self.player_event = False
            world.update(self.player_event)
            pg.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    play = Platformer(screen, WIDTH, HEIGHT)
    play.main()