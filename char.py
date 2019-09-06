# the main character class

import pygame as pg

from sprites import *

class Char(pg.sprite.Sprite):
    # the main character
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super(Char, self).__init__(self.groups)
        self.game = game
        self.walking = False
        self.facing = 'down'
        self.current_frame = 0
        self.last_updated = 0
        self.get_images()
        self.image = self.walking_animation_d[0]
        self.rect = self.image.get_rect()
        self.hit_box =  mc_hit_box
        self.hit_box.center = self.rect.center
        self.vx, self.vy = 0, 0
        self.x = x 
        self.y = y 
        self.hp = mc_hp
        self.mhp = mc_mhp
        self.att = mc_att
        self.invincible = False
        self.invincible_timer = 0
        self.stunned_timer = 0
        self.alive = True
        self.stunned = False
        self.knockback = mc_knockback
        self.attacking = False
        self.attack_timer = 0
        self.level = 1
        self.mexp = 5
        self.exp = 0

    def get_images(self):
        # get walking, standing, and attacking animations 
        # put them in lists
        self.walking_animation_l = []
        self.walking_animation_r = []
        self.walking_animation_u = []
        self.walking_animation_d = []

        sprite_sheet = SpriteSheet(mc_gfx)
        # down facing
        image = sprite_sheet.get_image(0, 0, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(16, 0, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(32, 0, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(48, 0, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_d.append(image)
        # right facing
        image = sprite_sheet.get_image(0, 32, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(16, 32, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(32, 32, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(48, 32, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_r.append(image)
        # up facing
        image = sprite_sheet.get_image(0, 64, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(16, 64, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(32, 64, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(48, 64, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_u.append(image)
        # left facing
        image = sprite_sheet.get_image(0, 96, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(16, 96, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(32, 96, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(48, 96, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.walking_animation_l.append(image)

        # attacking animation
        self.attacking_animation_l = []
        self.attacking_animation_r = []
        self.attacking_animation_u = []
        self.attacking_animation_d = []

        sprite_sheet = SpriteSheet(mc_gfx)
        # down facing
        image = sprite_sheet.get_image(8, 128, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_d.append(image)
        image = sprite_sheet.get_image(40, 128, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_d.append(image)
        image = sprite_sheet.get_image(72, 128, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_d.append(image)
        image = sprite_sheet.get_image(104, 128, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_d.append(image)
        # up facing
        image = sprite_sheet.get_image(8, 160, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_u.append(image)
        image = sprite_sheet.get_image(40, 160, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_u.append(image)
        image = sprite_sheet.get_image(72, 160, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_u.append(image)
        image = sprite_sheet.get_image(104, 160, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_u.append(image)
        # right facing
        image = sprite_sheet.get_image(8, 192, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_r.append(image)
        image = sprite_sheet.get_image(40, 192, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_r.append(image)
        image = sprite_sheet.get_image(72, 192, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_r.append(image)
        image = sprite_sheet.get_image(104, 192, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_r.append(image)
        # left facing
        image = sprite_sheet.get_image(8, 224, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_l.append(image)
        image = sprite_sheet.get_image(40, 224, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_l.append(image)
        image = sprite_sheet.get_image(72, 224, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_l.append(image)
        image = sprite_sheet.get_image(104, 224, 16, 32)
        image = pg.transform.scale(image, (int(tile_size / 2), 
                                    int(tile_size)))
        self.attacking_animation_l.append(image)


    def get_keys_x(self):
        # handle horizontal input
        self.vx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            if not self.stunned and not self.attacking:
                self.vx = -mc_movespeed
                self.facing = 'left'
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            if not self.stunned and not self.attacking:
                self.vx = mc_movespeed
                self.facing = 'right'
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def get_keys_y(self):
        # handle vertical input
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            if not self.stunned and not self.attacking:
                self.vy = -mc_movespeed
                self.facing = 'up'
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            if not self.stunned and not self.attacking:
                self.vy = mc_movespeed
                self.facing = 'down'
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def get_keys_misc(self):
        # handle all non-movement inputs
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.attack_timer > fb_rate:
                self.attack_timer = now
                Fireball(self.game, self.x, self.y, self.facing)

    def get_keys(self):
        # run all imput functions
        self.get_keys_y()
        self.get_keys_x()
        self.get_keys_misc()

    def update(self):
        self.check_cc()
        self.get_keys()
        self.animate()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.hit_box.centerx = self.x
        # obj collision
        obj_collision(self, self.game.walls, 'x')
        self.hit_box.centery = self.y
        obj_collision(self, self.game.walls, 'y')
        self.rect.center = self.hit_box.center
        # mob collision
        mob_collision(self, self.game.spooky_logs, 'x')
        self.hit_box.centery = self.y
        mob_collision(self, self.game.spooky_logs, 'y')
        self.rect.center = self.hit_box.center

    def animate(self):
        # animate mc depending on input
        now = pg.time.get_ticks()
        if self.vx != 0 or self.vy != 0:
            self. walking = True
        else:
            self.walking = False
        if not self.walking and not self.attacking:
            if self.facing == 'down':
                self.image = self.walking_animation_d[0]
            if self.facing == 'right':
                self.image = self.walking_animation_r[0]
            if self.facing == 'up':
                self.image = self.walking_animation_u[0]
            if self.facing == 'left':
                self.image = self.walking_animation_l[0]
        if self.walking:
            if now - self.last_updated > (mc_movespeed):
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(
                                    self.walking_animation_d)
                if self.facing == 'down':
                    self.image = self.walking_animation_d[self.current_frame]
                if self.facing == 'right':
                    self.image = self.walking_animation_r[self.current_frame]
                if self.facing == 'up':
                    self.image = self.walking_animation_u[self.current_frame]
                if self.facing == 'left':
                    self.image = self.walking_animation_l[self.current_frame]
        if self.attacking:
            if now - self.last_updated > (mc_att_speed):
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(
                                    self.attacking_animation_d)
                if self.facing == 'down':
                    self.image = self.attacking_animation_d[self.current_frame]
                if self.facing == 'right':
                    self.image = self.attacking_animation_r[self.current_frame]
                if self.facing == 'up':
                    self.image = self.attacking_animation_u[self.current_frame]
                if self.facing == 'left':
                    self.image = self.attacking_animation_l[self.current_frame]

    def check_cc(self):
        # check for character cc and work timer
        if self.invincible_timer == 60:
            self.invincible = False
        else:
            self.invincible_timer += 1 
        if self.stunned_timer == 5:
            self.stunned = False
        else:
            self.stunned_timer += 1

    def check_level_up(self):
        # check exp/mhp for level up conditions
        if self.exp >= self.mexp:
            self.exp -= self.mexp
            self.mexp *= 1.2
            self.mexp = int(self.mexp)
            self.level += 1
            self.att += 1
            self.mhp +=10
            self.hp = self.mhp