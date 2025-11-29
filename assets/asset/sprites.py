import pygame, sys
from config import *
from pygame.math import Vector2 as vector

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, surface, groups):
        # initialize the parent class
        super().__init__(groups)
        self.image = pygame.surface((TILE,TILE))
        self.image.fill('white')
        self.rect =self.image.get_rect(topleft=position)
    