import pygame
from background_file import make_background
from back import *
from players import Player
from bad_guy import Badguy
from player_health import Heathbar


# pygame setup
pygame.init()
#dimension(set up as your screen )
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#clock is for frame rate(slow and fast of the game)
clock = pygame.time.Clock()
# flag to make it run the whole time
running = True
# make the background
background = make_background()
# make a player here
player = Player()
badguy = Badguy()
health = Heathbar(50,25,100,25,100)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #pass the event to our player
    
    player.update_event()

    # update
    player.update()
    badguy.update()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE
    player.draw(screen)
    badguy.draw(screen)
    health.update(screen)


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()