import pygame
from back import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self,tmx_map):
        self.display_surface = pygame.get_surface()

        self.setup(tmx_map)

    def setup(self,tmx_map):
        for x, y in tmx_map.get_layer('Terrain').titles():
            print(x)
            print(y)
            print(surf)
    
    def update(self):
        self.display_surface.fill('red')