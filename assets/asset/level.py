import pygame, sys
from sprites import Sprite
from config import *
from pytmx import load_pygame
from pygame.math import Vector2 as vector

class Level():
    def __init__(self, tmx_map):
        self.display_surface=pygame.display.get_surface()

        # create groups
        self.all_sprites= pygame.sprite.Group()

        self.update(tmx_map)


    def update(self,tmx_map):
        # looping through the tile map
        for x,y,surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x*TILE,y*TILE),surf, self.all_sprites)
    def draw(self):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        
        