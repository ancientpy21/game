import pygame

class Music:
    def __init__(self):
        pygame.mixer.init()

        self.start = pygame.mixer.Sound("start.wav")
        self.lose = pygame.mixer.Sound("lose.wav")

    def play_start(self):
        self.start.play()

    def play_lose(self):
        self.lose.play()