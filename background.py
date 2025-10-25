
import pygame
from back import *

class Scrolling:
    def __init__(self, image_path, speed=0.5):
        self.speed = speed
        self.scroll_x = 0

        # load image 
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image,(WIDTH,HEIGHT))
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()

        # background surface
        self.background = pygame.Surface((WIDTH, HEIGHT))
        for x in range(0, WIDTH, self.image_width):
            for y in range(0, HEIGHT, self.image_height):
                self.background.blit(self.image, (x, y))
    # make the scrolling effect
    def update(self):
        self.scroll_x -= self.speed
        if self.scroll_x <= -self.image_width:
            self.scroll_x = 0
    # draw it to the screen or blit
    def draw(self, screen):
        # draw the scrolling background
        screen.blit(self.background, (self.scroll_x, 0))
        screen.blit(self.background, (self.scroll_x + self.image_width, 0))
