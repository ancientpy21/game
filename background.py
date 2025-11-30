import pygame
from config import *
# Load a single tile image from file
class Background:
    def __init__(self):
        self.tile = pygame.image.load("assets/asset/game file/Background/Blue.png").convert_alpha()
        self.tile_w, self.tile_h = self.tile.get_size()

        # Pre-render background to a single surface
        self.bg_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        for y in range(0, HEIGHT, self.tile_h):
            for x in range(0, WIDTH, self.tile_w):
                self.bg_surface.blit(self.tile, (x, y))

    def draw(self, screen):
        screen.blit(self.bg_surface, (0, 0))

