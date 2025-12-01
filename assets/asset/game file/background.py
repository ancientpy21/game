import pygame
from config import *

class Background:
    def __init__(self, image_path, width, height, floor_y, floor_color=(0, 0, 0)):
        # Load and scale the background image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.width = width
        self.height = height
        self.floor_y = floor_y
        self.floor_color = floor_color

    def draw(self, screen):
        # Draw the background image
        screen.blit(self.image, (0, 0))
        # Draw the floor line
        pygame.draw.line(screen, self.floor_color, (0, self.floor_y), (self.width, self.floor_y), 5)
