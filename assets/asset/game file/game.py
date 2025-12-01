
import pygame
import sys
from background import Background
from config import *
from players import Player
from main_menu import StartScreen
from score import Score
from enemies import Enemy
from game_over import GameOver

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

# MAIN MENU
start_screen = StartScreen(screen)
start_screen.run()

# make the background
bg = Background(image_path='abc.jpg', width=WIDTH, height=HEIGHT, floor_y=FLOOR_Y, floor_color=(0,0,0))
score =Score()

# GAME OBJECT
player = Player(100, FLOOR_Y - 50)
enemies = pygame.sprite.Group()
enemies.add(Enemy())
enemies.add(Enemy(speed=2))

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    if pygame.sprite.spritecollide(player, enemies, False):
        gameover_sc= GameOver(screen)
        gameover_sc.run(score.value)
        running=False
        


    bg.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    score.draw(screen)


    score.update()
    player.update()
    enemies.update()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
sys.exit()