import pygame
from config import *
from pytmx.util_pygame import load_pygame
from tile_class import Tile


class Level():
    def __init__(self, screen):
        self.screen =screen
        self.offset=[0,0]
        self.levelData=load_pygame("assets/asset/level/basic.tmx")
        self.platformtiles = pygame.sprite.Group()

        layer = self.levelData.get_layer_by_name('Terrain')

        self.level_width = self.levelData.width * TILE
        self.level_height = self.levelData.height * TILE
        
        for x,y , tilesurf in layer.tiles():
            tile=Tile((x*TILE,y*TILE),tilesurf)
            self.platformtiles.add(tile)

    def set_offset(self,off_x,off_y):
        self.offset[0] = off_x
        self.offset[1]= off_y
    def follow_player(self, player):
        # Center camera on player
        off_x = player.x - WIDTH // 2
        off_y = player.y - HEIGHT // 2

        # Clamp to map edges
        off_x = max(0, min(off_x, self.level_width - WIDTH))
        off_y = max(0, min(off_y, self.level_height - HEIGHT))

        self.set_offset(off_x, off_y)
    def update(self):
        pass

    def draw(self):
        for tile in self.platformtiles:
            tile.draw(self.screen,self.offset)
    def run(self,player):
        self.follow_player(player)
        self.update()
        self.draw()