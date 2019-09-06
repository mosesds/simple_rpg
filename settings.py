# all settings and base stats for main character/mobs

import pygame as pg

# define some colors
black = (0, 0, 0)
light_grey = (100, 100, 100)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
light_blue = (0, 191, 255)

# game settings
screen_width = 640   
screen_height = 480  
fps = 60
title = 'First Side Project (Game #1)' 
tile_size = 32

# main character settings
mc_movespeed = 125
mc_gfx = 'character.png'
mc_hit_box = pg.Rect(0, 5, 16, 16)
mc_hp = 100
mc_mhp = 100
mc_att = 25
mc_knockback = 25
mc_att_speed = 25

# spooky Log settings
sl_movespeed = 50
sl_gfx = 'spooky_log.png'
sl_hit_box = pg.Rect(0, 0, 16, 16)
sl_mhp = 50
sl_hp = 50
sl_att = 25
sl_knockback = 20
sl_exp = 1

# fireball settings
fb_speed = 500
fb_duration = 1000
fb_hit_box = pg.Rect(0, 0, 8, 8)
fb_rate = 1000

# hud settings
mc_hud_gfx = 'objects.png'