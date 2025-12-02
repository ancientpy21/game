import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()

        self.start = pygame.mixer.Sound("sci_fi_theme.mp3")
        self.lose = pygame.mixer.Sound("explosionCrunch_001.ogg")

    def play_start(self):
        self.start.play()

    def play_lose(self):
        self.lose.play()

    def stop_music(self):
        pygame.mixer.music.stop()