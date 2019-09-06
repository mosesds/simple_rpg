# all sprites except the main character

import pygame as pg

from os import path
from random import choice

from settings import *
from map import collide_hit_box
from collisions import mob_collision, obj_collision

class SpriteSheet(object):
    # get image from sprite sheet and set transparent color
    # needs location and dimensions of sprite
    def __init__(self, file_name): 
        self.sprite_sheet = pg.image.load(path.join('gfx', 
                            file_name)) .convert()

    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(black)
        image = pg.transform.scale(image, (int(tile_size), 
                int(tile_size)))
        return image

class Obstacle(pg.sprite.Sprite):
    # anything that cant be walked over
    # currently all considered walls
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        super(Obstacle, self).__init__(self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y

class SpookyLog(pg.sprite.Sprite):
    # the enemy mob, a non-aggro ghost log
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.spooky_logs
        super(SpookyLog, self).__init__(self.groups)
        self.game = game
        self.walking = False
        self.facing = 'down'
        self.current_frame = 0
        self.last_updated = 0
        self.get_images()
        self.image = self.walking_animation_d[0]
        self.rect = self.image.get_rect()
        self.hit_box =  sl_hit_box.copy()
        self.hit_box.center = self.rect.center
        self.vx, self.vy = 0, 0
        self.x = x 
        self.y = y
        self.hp = sl_hp
        self.mhp = sl_mhp
        self.att = sl_att 
        self.knockback = sl_knockback
        self.exp = sl_exp

    def get_images(self):
        # grabs the sprites for animation anf puts them in a list 
        self.walking_animation_l = []
        self.walking_animation_r = []
        self.walking_animation_u = []
        self.walking_animation_d = []

        sprite_sheet = SpriteSheet(sl_gfx)
        # down facing
        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(64, 0, 32, 32)
        self.walking_animation_d.append(image)
        image = sprite_sheet.get_image(96, 0, 32, 32)
        self.walking_animation_d.append(image)
        # right facing
        image = sprite_sheet.get_image(0, 32, 32, 32)
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(32, 32, 32, 32)
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(64, 32, 32, 32)
        self.walking_animation_r.append(image)
        image = sprite_sheet.get_image(96, 32, 32, 32)
        self.walking_animation_r.append(image)
        # up facing
        image = sprite_sheet.get_image(0, 64, 32, 32)
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(32, 64, 32, 32)
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(64, 64, 32, 32)
        self.walking_animation_u.append(image)
        image = sprite_sheet.get_image(96, 64, 32, 32)
        self.walking_animation_u.append(image)
        # left facing
        image = sprite_sheet.get_image(0, 96, 32, 32)
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        self.walking_animation_l.append(image)
        image = sprite_sheet.get_image(96, 96, 32, 32)
        self.walking_animation_l.append(image)

    def update(self):
        self.check_for_mc()
        self.mob_ai()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.hit_box.centerx = self.x
        obj_collision(self, self.game.walls, 'x')
        self.hit_box.centery = self.y
        obj_collision(self, self.game.walls, 'y')
        self.rect.center = self.hit_box.center

    def check_for_mc(self):
        # check if mc is nearby and set walking accordingly
        if abs(self.game.mc.x - self.x) < 3 * tile_size and abs(self.game.mc.y 
                - self.y) < 3 * tile_size:
            self.walking = True
        else:
            self.walking = False

    def mob_ai(self):
        # decides action based on if the mob is considered "walking"
        now = pg.time.get_ticks()
        dir_list = ['up', 'down', 'left', 'right']
        if not self.walking:
            if now - self.last_updated > (sl_movespeed * 16):
                self.last_updated = now
                self.facing = choice(dir_list)
                if self.facing == 'down':
                    self.image = self.walking_animation_d[0]
                if self.facing == 'right':
                    self.image = self.walking_animation_r[0]
                if self.facing == 'up':
                    self.image = self.walking_animation_u[0]
                if self.facing == 'left':
                    self.image = self.walking_animation_l[0]
        else:
            if now - self.last_updated > (sl_movespeed * 8):
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(
                                    self.walking_animation_d)
                self.facing = choice(dir_list)
                self.vx, self.vy = 0, 0
                if self.facing == 'down':
                    self.vy = sl_movespeed
                    self.image = self.walking_animation_d[self.current_frame]
                if self.facing == 'right':
                    self.vx = sl_movespeed
                    self.image = self.walking_animation_r[self.current_frame]
                if self.facing == 'up':
                    self.vy = -sl_movespeed
                    self.image = self.walking_animation_u[self.current_frame]
                if self.facing == 'left':
                    self.vx = -sl_movespeed
                    self.image = self.walking_animation_l[self.current_frame]
                if self.vx != 0 and self.vy != 0:
                    self.vx *= 0.7071
                    self.vy *= 0.7071

    def draw_hp_bar(self):
        # draw mob hp bar if it has taken damage
        if self.hp > self.mhp * 0.66:
            color = green
        if self.hp > self.mhp * 0.33:
            color = yellow
        else:
            color = red
        hp_width = int(self.rect.width * (self.hp / self.mhp))
        mhp_width = int(self.rect.width * self.mhp)
        self.hp_bar = pg.Rect(0, 0, hp_width, 5)
        self.mhp_bar = pg.Rect(0, 0, mhp_width, 5)
        if self.hp < self.mhp:
            pg.draw.rect(self.image, light_grey, self.mhp_bar)
            pg.draw.rect(self.image, color, self.hp_bar)

class Fireball(pg.sprite.Sprite):
    # create fireball projectile and allow it to move in specified direction
    def __init__(self, game, x, y, facing):
        self.groups = game.all_sprites, game.fireballs
        super(Fireball, self).__init__(self.groups)
        self.game = game
        sprite_sheet = SpriteSheet(mc_hud_gfx)
        self.image = sprite_sheet.get_image(191, 48, 17, 17)
        self.rect = self.image.get_rect()
        self.hit_box =  sl_hit_box.copy()
        self.hit_box.center = self.rect.center
        self.vx, self.vy = fb_speed, fb_speed
        self.x = x 
        self.y = y
        self.duration = pg.time.get_ticks()
        self.facing = facing

    def update(self):
        self.move()
        self.rect = self.image.get_rect()
        self.hit_box.centerx = self.x
        self.hit_box.centery = self.y
        self.rect.center = self.hit_box.center
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.duration > fb_duration:
            self.kill()

    def move(self):
        if self.facing == 'down':
            self.y += self.vy * self.game.dt
        if self.facing == 'up':
            self.y -= self.vy * self.game.dt
        if self.facing == 'right':
            self.x += self.vx * self.game.dt
        if self.facing == 'left':
            self.x -= self.vx * self.game.dt

class Direction():
    # instance the dir for when we want the dir determined only once
    def __init__(self, facing):
        self.direction = facing

    def return_dir(self):
        return self.facing

def combat(game):
    # take hp from mob, kill, respawn if collision will fireballs
    hits = pg.sprite.groupcollide(game.spooky_logs, game.fireballs, 
                                        False, True)
    for hit in hits:
        hit.hp -= game.mc.att
        if hit.hp <= 0:
            game.mc.exp += hit.exp
            game.mc.check_level_up()
            hit.kill()
            for tile_obj in game.map.tmx_data.objects:
                if tile_obj.name == 'spooky_log':
                    SpookyLog(game, tile_obj.x, tile_obj.y) 