import pygame
from config import *
image_path='abc.jpg'
class Background:
    def __init__(self, image_path, width, height):
        # Load and scale the background image
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (width,height))

    def draw(self, screen):
        # Draw the background on the screen
        screen.blit(self.image, (0, 0))