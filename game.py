import pygame
from background import Scrolling
from back import *


# pygame setup
pygame.init()
#dimension(set up as your screen )
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#clock is for frame rate(slow and fast of the game)
clock = pygame.time.Clock()
# flag to make it run the whole time
running = True
# make the background
bg= Scrolling('assets/1 Layer Night sea.png')

bg2=Scrolling('assets/2 Layer River.png')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    bg.update()
    bg.draw(screen)
    
    # RENDER YOUR GAME HERE

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()