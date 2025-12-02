import pygame
from config import *

class Score:
    def __init__(self, font_size=30, color=(255,255,255), x=10, y=10):
        self.points = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color
        self.x = x
        self.y = y
        self.increment = 0.1 # make it faster/ slower here
        self.last_update = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >=1:
    
            # Increase points every second
            self.points += self.increment

    def draw(self, screen):
        text = self.font.render(f"Score: {int(self.points)}", True, self.color)
        screen.blit(text, (self.x, self.y))