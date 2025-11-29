# import here
import pygame, sys
from config import *
#from pygame.math import Vector2 as vector
# using class to make clearer 


class Game:
    def __init__(self):
        #initialize here
        pygame.init()
        # Setup the display surface using constants from config.py
        self.display_surface =pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Platformer')

    # here for the running event to display
    def run(self):
        # make a smoother frame rate
        dt = self.clock.tick(FPS) 
        # loop the game
        while True:

            self.clock = pygame.time.Clock()
            for event in pygame.event.get():
                if pygame.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.display_surface.fill('white')
            pygame.display.update()

# create instance to execute Game
if __name__ == '__main__':
    game = Game()
    game.run()