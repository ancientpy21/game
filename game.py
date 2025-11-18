import pygame
from background_file import make_background
from back import *
from players import Player
from bad_guy import Badguy
from player_health import Heathbar
from random import randint


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
badguy_group= pygame.sprite.Group()
# make a player here
player = Player(badguy_group,background)

for i in range(3):
    badguy_group.add(Badguy(player))

health = Heathbar(50,25,150,25,100)

screen_num=0
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
    badguy_group.update()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE
    player.draw(screen)
    badguy_group.draw(screen)
    health.update(screen,player.hp)


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()