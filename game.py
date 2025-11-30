
import pygame
import sys
from background import load_background,draw_background
from config import *
from players import Player


# pygame setup
pygame.init()
#dimension(set up as your screen )
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# set caption
pygame.display.set_caption('Platformer')
#clock is for frame rate(slow and fast of the game)
clock = pygame.time.Clock()
# flag to make it run the whole time
running = True


# make the background
bg =load_background()
player = Player((WIDTH / 2, HEIGHT - 50), True) 

screen_num=0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    player.update(level=None) 

    
    
    
    
    draw_background(screen,bg)
    player.draw(level=None)
 


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()