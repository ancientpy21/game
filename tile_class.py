import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, surface, scale=1):
        super().__init__()
        w = surface.get_width() * scale
        h = surface.get_height() * scale
        self.image = pygame.transform.scale(surface, (w, h))

        self.rect = self.image.get_rect(topleft=position)
        

    def draw(self, screen, offset):
        screen.blit(self.image, (self.rect.x - offset[0], self.rect.y - offset[1]))