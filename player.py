import pygame as pg
from support import import_sprite

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self._import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pg.mask.from_surface(self.image)

        self.direction = pg.math.Vector2(0,0)
        self.speed = 5
        self.jump_move = -16

        self.life = 5
        self.game_over = False
        self.win = False
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_celling = False
        self.on_left = False
        self.on_right = False

    def _import_character_assets(self):
        charcter_path = "Assets/Player"
        self.animations = {"Idle": [], "Walk":[], "jump":[], "FALL":[], "Diw":[], "Win":[]}
        for animation in self.animations.keys():
            full_path = charcter_path +animation
            self.animations[animation] = import_sprite(full_path)

    def _animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        image = pg.transform.scale(image, (35,50))
        if self.facing_right: 
            self.image = image
        else: 
            flipped_image = pg.transform.flip(image, True, False)
            self.image = flipped_image
        
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_celling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_celling and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.topleft)
        elif self.on_celling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def _get_input(self, player_event):
        if player_event != False:
            if player_event == "right":
                self.direction.x = 1
                self.facing_right = True
            elif player_event == "left":
                self.direction.x = -1
                self.facing_right = False
        else:
            self.direction.x = 0

    def _jump(self):
        self.direction.y = self.jump_move

    def _get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "FALL"
        elif self.direction.x != 0:
            self.status = "Walk"
        else:
            self.status = "Idle"

    def update(self, player_event):
        self._get_status()
        if self.life > 0 and not self.game_over:
            if player_event == "space" and self.on_ground:
                self._jump()
            else:
                self._get_input(player_event)
        elif self.game_over and self.win:
            self.direction.x = 0
            self.status = "Win"
        else:
            self.direction.x = 0
            self.status = "Die"
        self._animate()