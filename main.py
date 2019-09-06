#! python3
# simple rpg; kill the mobs, level up, don't die.

import pygame as pg
import sys

from os import path

from settings import *
from sprites import *
from map import *
from char import Char
from hud import *
from collisions import *

class Game:
    def __init__(self):
        # initialize everything needed in the bg
        pg.init()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.clock = pg.time.Clock()
        pg.display.set_caption(title)
        self.load_data()

    def load_data(self):
        # sets up paths and loads map
        game_folder = path.dirname(__file__)
        gfx_folder = path.join(game_folder, 'gfx')
        map_folder = path.join(game_folder, 'maps')
        self.map = Map(path.join(map_folder, 'spawn.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.spooky_logs = pg.sprite.Group()
        self.fireballs = pg.sprite.Group()
        for tile_obj in self.map.tmx_data.objects:
            if tile_obj.name == 'spawn':
                self.mc = Char(self, tile_obj.x, tile_obj.y)
            if tile_obj.name == 'spooky_log':
                SpookyLog(self, tile_obj.x, tile_obj.y)  
            if tile_obj.name == 'log' or tile_obj.name == 'rock':
                Obstacle(self, tile_obj.x, tile_obj.y,
                        tile_obj.width, tile_obj.height)
            if tile_obj.name == 'water' or tile_obj.name == 'house':
                Obstacle(self, tile_obj.x, tile_obj.y,
                        tile_obj.width, tile_obj.height)
            if tile_obj.name == 'bush' or tile_obj.name == 'border':
                Obstacle(self, tile_obj.x, tile_obj.y,
                        tile_obj.width, tile_obj.height)
        self.fov = FOV(self.map.width, self.map.height)

    def run(self):
        # game loop 
        while self.mc.alive:
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.fov.update(self.mc)
        combat(self)

    def draw(self):
        # draw everything then flip display
        self.screen.blit(self.map_img, self.fov.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            if isinstance(sprite, SpookyLog):
                sprite.draw_hp_bar()
            self.screen.blit(sprite.image, self.fov.apply(sprite))
        # HUD
        draw_hud_bg(self.screen, self.fov.apply(sprite), 0, 0)
        draw_mc_hp(self.screen, self.fov.apply(sprite), 12, 
                    12, self.mc.hp / self.mc.mhp)
        draw_iframes(self.screen, self.fov.apply(sprite), 6, 
                        102, self.mc)
        draw_mc_level(self.screen, self.fov.apply(sprite), 10, 60, self.mc.level)
        draw_exp_bar(self.screen, 49, 82, self.mc.exp / self.mc.mexp)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

# create a game instance
g = Game()
while True:
    g.new()
    g.run()