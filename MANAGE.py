import pygame
from config import *



class SpriteSheet():
    def __init__(self,path, positions):
        image = pygame.image.load(path).convert_alpha()
        self.sprites =[]
        self.spriteflipped =[]

        for position in positions:
            sprite = image.subsurface(pygame.Rect(position))
            self.sprites.append(sprite)
            flipped = pygame.transform.flip(sprite,True,False)
            self.spriteflipped.append(flipped)


    def getSprites(self, flipped):
        if flipped== True:
            return self.spriteflipped
        else:
            return self.sprites


