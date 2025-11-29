import pygame
from back import *
# Load a single tile image from file
def load_tile(path):
    tile = pygame.image.load(path).convert()
    return tile


# Create a full background made from many small tiles
def load_background():
    # Load the small tile image
    tile = load_tile('assets/asset/game file/Background/Blue.png')

    tile_w = tile.get_width()
    tile_h = tile.get_height()

    # Create surface the size of the screen
    bg = pygame.Surface((WIDTH, HEIGHT))

    # Tile it across the screen
    for y in range(0, HEIGHT, tile_h):
        for x in range(0, WIDTH, tile_w):
            bg.blit(tile, (x, y))

    return bg


def draw_background(screen, bg):
    screen.blit(bg, (0,0))



