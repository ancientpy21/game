import pygame
from sys import exit
from config import *

class StartScreen:
    def __init__(self, screen, width=WIDTH, height=HEIGHT, button_text="START GAME"):
        self.screen = screen
        self.width = width
        self.height = height
        self.button_text_str = button_text
        self.clock = pygame.time.Clock()

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BUTTON_COLOR = (70, 130, 180)
        self.BUTTON_HOVER = (100, 160, 210)

        # Font
        self.font = pygame.font.SysFont(None, 50)

        # Button setup
        self.button_text = self.font.render(self.button_text_str, True, self.WHITE)
        self.button_rect = self.button_text.get_rect(center=(self.width // 2, self.height // 2))

    def run(self):
        
        running = True
        while running:
            self.screen.fill(self.BLACK)
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            # Draw button with hover effect
            if self.button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, self.BUTTON_HOVER, self.button_rect.inflate(20, 20))
                if mouse_click[0]:  # left click
                    running = False
            else:
                pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.button_rect.inflate(20, 20))

            # Draw button text
            self.screen.blit(self.button_text, self.button_rect)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(60)