import pygame
import sys
from background import Background
from config import *
from players import Player
from main_menu import StartScreen
from score import Score
from enemies import Enemy
from game_over import GameOver
from play_music import Music

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
# Music here
play=Music()


# MAIN MENU



# make the background
while True:  # Main program loop
    # 1. Start screen
    start_screen = StartScreen(screen)
    start_screen.run()
    play.play_start()
    
    # 2. Initialize game objects
    bg = Background(image_path='abc.jpg', width=WIDTH, height=HEIGHT, floor_y=FLOOR_Y, floor_color=(0,0,0))
    score = Score()
    player = Player(100, FLOOR_Y - 50)
    enemies = pygame.sprite.Group()
    for i in range(5):
        enemies.add(Enemy(x=WIDTH + i*150))
    enemies.add(Enemy(speed=3, x=WIDTH + 800))
    
    # 3. Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()
        enemies.update()
        score.update()
        
        # Collision check
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                play.stop_music()
                play.play_lose()
                # Show Game Over screen
                GameOver(screen).run(int(score.points))
                running = False
                break

        # Draw
        bg.draw(screen)
        player.draw(screen)
        enemies.draw(screen)
        score.draw(screen)

        pygame.display.flip()
        clock.tick(60)
