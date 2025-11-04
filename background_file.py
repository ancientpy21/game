import pygame
from back import *

def make_background():
    #make a terrain background
    terrain_loc='assets/asset/terrain.png'
    terrain= pygame.image.load(terrain_loc).convert_alpha()
    terrain= pygame.transform.scale(terrain,(WIDTH,HEIGHT))

    # get width and height
    terrain_width= terrain.get_width()
    terrain_height= terrain.get_height()

    # make new surface
    background= pygame.Surface((WIDTH,HEIGHT))

    #loop over the background and place tile on it
    for x in range(0,WIDTH,terrain_width):
        for y in range(0,HEIGHT,terrain_height):
            background.blit(terrain, (x,y))
    # if there is more background loop over it too
    
    # return
    return background

        