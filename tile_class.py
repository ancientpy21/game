import pygame
import csv
from config import *


# ---------------------------------------------------
# TILE CLASS (each block in the map)
# ---------------------------------------------------
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE, TILE))
        self.image.fill((120, 200, 120))  # TEMP block color
        self.rect = self.image.get_rect(topleft=(x, y))


# ---------------------------------------------------
# READ CSV FILE INTO A LIST
# ---------------------------------------------------
def load_csv(path):
    layout = []
    with open(path, newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            layout.append(row)
    return layout


# ---------------------------------------------------
# CREATE LEVEL FROM CSV
# ---------------------------------------------------
def load_level(csv_path="assets/asset/level/tile 1.csv"):
    tile_group = pygame.sprite.Group()

    layout = load_csv(csv_path)

    for row_index, row in enumerate(layout):
        for col_index, cell in enumerate(row):
            if cell == "1":
                x = col_index * TILE
                y = row_index * TILE
                tile = Tile(x, y)
                tile_group.add(tile)

    return tile_group