import pygame
from back import*


class MainText:
    def __init__(self):
        # Title
        self.title_font = pygame.font.Font('assets/fonts/SuperAdorable-MAvyp.ttf', 64)
        self.green = (0,0,250)
        self.title_surface = self.title_font.render('MONSTERS', True, self.green)
        self.title_rect = self.title_surface.get_rect(center=(WIDTH/2, HEIGHT/2))

        # Game Over
        self.end_font = pygame.font.Font('assets/fonts/SuperAdorable-MAvyp.ttf', 64)
        self.red = (250,0,0)
        self.end_surface = self.end_font.render('GAME OVER', True, self.red)
        self.end_rect = self.end_surface.get_rect(center=(WIDTH/2, HEIGHT/2))

        # self.death_time = 3000  # fade duration in milliseconds
        # self.birth_time = pygame.time.get_ticks()
        self.game_over = False
        self.title= True

    def update(self):
        # Fade out title as i click
        if pygame.mouse.get_pressed()[0]:
            self.title =False
    def draw_title(self, screen):
        if self.title:
            screen.blit(self.title_surface, self.title_rect)

    def update_game(self, hp):
        if hp <= 0:
            self.game_over = True

    def draw_game_over(self, screen):
        if self.game_over:
            screen.blit(self.end_surface, self.end_rect)