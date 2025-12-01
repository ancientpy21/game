import pygame
from config import *
from main_menu import StartScreen
from game import run_game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Show start menu first
StartScreen(screen).run()

# Run the main game loop repeatedly
while True:
    run_game(screen)