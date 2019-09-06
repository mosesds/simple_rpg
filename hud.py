# all hud images and rendering

from sprites import SpriteSheet
from settings import *

def draw_mc_hp(surface, destination, x, y, perc_hp):
    # draw hearts in mc fov, updates in quarter incriments
    if perc_hp < 0:
        perc_hp = 0
    sprite_sheet = SpriteSheet(mc_hud_gfx)
    full_image = sprite_sheet.get_image(63, 0, 16, 16)
    three_quarters_image = sprite_sheet.get_image(79, 0, 16, 16)
    half_image = sprite_sheet.get_image(95, 0, 16, 16)
    quarter_image = sprite_sheet.get_image(111, 0, 16, 16)    
    empty_image = sprite_sheet.get_image(127, 0, 16, 16)
    if perc_hp == 1.0:
        image = full_image
    elif perc_hp > .75:
        image = three_quarters_image
    elif perc_hp > .50:
        image = half_image
    elif perc_hp > .25:
        image = quarter_image
    else: 
        image = empty_image
    surface.blit(image, [x, y])

def draw_mc_level(surface, destination, x, y, level):
    # draws numbers represeting the level, currently capped at 9
    # displays a 0 for anything above 9
    sprite_sheet = SpriteSheet(mc_hud_gfx)
    images = [
        sprite_sheet.get_image(80, 224, 16, 16),
        sprite_sheet.get_image(96, 224, 16, 16),
        sprite_sheet.get_image(112, 224, 16, 16),
        sprite_sheet.get_image(128, 224, 16, 16),
        sprite_sheet.get_image(80, 240, 16, 16),
        sprite_sheet.get_image(96, 240, 16, 16),
        sprite_sheet.get_image(112, 240, 16, 16),
        sprite_sheet.get_image(128, 240, 16, 16),
        sprite_sheet.get_image(80, 256, 16, 16),
        sprite_sheet.get_image(96, 256, 16, 16),
        ]
    if level <=9:
        image = images[level-1]
    else:
        image = images[:-1]   
    surface.blit(image, [x, y])

def draw_iframes(surface, destination, x, y, who):
    # draw invincibility buff when invincible
    sprite_sheet = SpriteSheet(mc_hud_gfx)
    image = sprite_sheet.get_image(229, 54, 5, 5)
    if who.invincible == True:
        surface.blit(image, [x, y])

def draw_exp_bar(surface, x, y, exp):
    # draw exp bar based on percentage (exp/mexp)
    if exp < 0:
        exp = 0
    color = light_blue
    width = 104 * exp
    exp_bar = pg.Rect(x, y, width, 3)
    pg.draw.rect(surface, color, exp_bar)

def draw_hud_bg(surface, destination, x, y):
    # draw the bg image for the rest of the hud
    sprite_sheet = SpriteSheet(mc_hud_gfx)
    image = sprite_sheet.get_image(0, 226, 16, 16)
    surface.blit(image, [x, y])
    image = sprite_sheet.get_image(0, 242, 16, 16)
    surface.blit(image, [x, y + 32])
    image = sprite_sheet.get_image(0, 258, 16, 16)
    surface.blit(image, [x, y + 64])
    image = sprite_sheet.get_image(0, 274, 16, 16)
    surface.blit(image, [x, y + 96])
    image = sprite_sheet.get_image(16, 226, 16, 16)
    surface.blit(image, [x + 32, y])
    image = sprite_sheet.get_image(16, 242, 16, 16)
    surface.blit(image, [x + 32, y + 32])
    image = sprite_sheet.get_image(16, 258, 16, 16)
    surface.blit(image, [x + 32, y + 64])
    image = sprite_sheet.get_image(16, 274, 16, 16)
    surface.blit(image, [x + 32, y + 96])
    image = sprite_sheet.get_image(32, 258, 16, 16)
    surface.blit(image, [x + 64, y + 64])
    image = sprite_sheet.get_image(48, 258, 16, 16)
    surface.blit(image, [x + 96, y + 64])
    image = sprite_sheet.get_image(64, 258, 16, 16)
    surface.blit(image, [x + 128, y + 64])