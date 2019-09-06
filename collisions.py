# sprite collision handling

import pygame as pg

from map import collide_hit_box
from settings import *

def obj_collision(sprite, group, dir):
    # handles collisions with objects, currently only walls group
    for wall in sprite.game.walls:
        if dir == 'x':
            hits = pg.sprite.spritecollide(sprite, group, False, 
                    collide_hit_box) 
            if hits:
                if hits[0].rect.centerx > sprite.hit_box.centerx:
                    sprite.x = hits[0].rect.left - sprite.hit_box.width / 2
                if hits[0].rect.centerx < sprite.hit_box.centerx:
                    sprite.x = hits[0].rect.right + sprite.hit_box.width / 2
                sprite.vx = 0
                sprite.hit_box.centerx = sprite.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite, group, False, 
                collide_hit_box) 
            if hits:
                if hits[0].rect.centery > sprite.hit_box.centery:
                    sprite.y = hits[0].rect.top - sprite.hit_box.width / 2
                if hits[0].rect.centery < sprite.hit_box.centery:
                    sprite.y = hits[0].rect.bottom + sprite.hit_box.width / 2
                sprite.vy = 0
                sprite.hit_box.centery = sprite.y

def mob_collision(sprite, group, dir):
    # handles collisions with mobs, currently only the spooky_logs group
    for sl in sprite.game.spooky_logs:
        hits = pg.sprite.spritecollide(sprite, group, False, 
                    collide_hit_box) 
        for hit in hits:
            # take dmg
            if sprite.invincible == False:
                sprite.hp -= sl_att
                if sprite.hp <= 0:
                    sprite.alive = False 
        if hits:
            if sprite.invincible == False:
                sprite.invincible = True
                sprite.invincible_timer = 0
            if sprite.stunned == False:
                sprite.stunned = True
                sprite.stunned_timer = 0
        if dir == 'x':
            if hits:
                if sprite.vx > 0:
                    sprite.x = hits[0].rect.left - hits[0].knockback
                    hits[0].walking = False
                if sprite.vx < 0:
                    sprite.x = hits[0].rect.right + hits[0].knockback
                    hits[0].walking = False
                sprite.vx = 0
                sprite.hit_box.centerx = sprite.x
        if dir == 'y':
            if hits:
                if sprite.vy > 0:
                    sprite.y = hits[0].rect.top - hits[0].knockback
                    hits[0].walking = False
                if sprite.vy < 0:
                    sprite.y = hits[0].rect.bottom + hits[0].knockback
                    hits[0].walking = False
                sprite.vy = 0
                sprite.hit_box.centery = sprite.y 