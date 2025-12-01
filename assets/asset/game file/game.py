import pygame
import sys
from background import Background
from config import *
from players import Player
from main_menu import StartScreen
from score import Score
from enemies import Enemy
from game_over import GameOver

# MAIN MENU

def run_game(screen):
    clock = pygame.time.Clock()
    # make the background
    bg = Background(image_path='abc.jpg', width=WIDTH, height=HEIGHT, floor_y=FLOOR_Y, floor_color=(0,0,0))
    score =Score()
    # GAME OBJECT
    player = Player(100, FLOOR_Y - 50)
    enemies = pygame.sprite.Group()
    for i in range(5):
        enemies.add(Enemy(x=WIDTH + i*150))
    enemies.add(Enemy(speed=3, x=WIDTH + 800))
    # GameOver object

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            if pygame.sprite.spritecollide(player, enemies, False):
                GameOver(screen).run(int(score.points))
                return 
            
            

        # Draw
        bg.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        score.draw(screen)

        # Update
        score.update()
        player.update()
        enemies.update()


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    sys.exit()