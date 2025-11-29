# import here
import pygame, sys
from config import *
from level import Level
# to import our tile from the tiled app
from pytmx.util_pygame import load_pygame
# to simplify the loading the file path
from os.path import join
from pygame.math import Vector2 as vector
# using class to make clearer 


class Game:
    def __init__(self):
        #initialize here
        pygame.init()
        # Setup the display surface using constants from config.py
        self.display_surface =pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Platformer')
        # load the map here
        self.tmx_map ={0: load_pygame(join("level", "basic.tmx"))}

        self.current_stage= Level(self.tmx_map[0])

    # here for the running event to display
    def run(self):
       
        # loop the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.current_stage.draw()
            self.display_surface.fill('black')
            pygame.display.update()

# create instance to execute Game
if __name__ == '__main__':
    game = Game()
    game.run()