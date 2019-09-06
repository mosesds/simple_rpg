# maps, and character fov

import pygame as pg
import pytmx

from settings import *

class Map:
    # makes an instance of the tmx file
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height *tm.tileheight
        self.tmx_data = tm

    def render(self, surface):
        # checks visible layers and blits each tile
        ti = self.tmx_data.get_tile_image_by_gid
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmx_data.tilewidth, 
                                            y * self.tmx_data.tileheight))

    def make_map(self):
        #actually makes the map using render() 
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class FOV:
    # creates the view that the player sees
    # centered on the player, except on map edges
    # offset the box when the player moves
    def __init__(self, width, height):
        self.fov = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.fov.topleft)

    def apply_rect(self, rect):
        return rect.move(self.fov.topleft)

    def update(self, target):
        x = -target.rect.x + int(screen_width / 2)
        y = -target.rect.y + int(screen_height / 2)

        # limit scrolling to map size (min/max coords)
        x = min(0, x)  
        y = min(0, y)  
        x = max(-(self.width - screen_width), x)  
        y = max(-(self.height - screen_height), y)  
        self.fov = pg.Rect(x, y, self.width, self.height)

def collide_hit_box(one, two):
    # intermediary to use hit_box instead of image rect
    return one.hit_box.colliderect(two.rect)