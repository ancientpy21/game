import pygame
from config import *



class SpriteSheet():
    def __init__(self,path, positions):
        # Load the full sprite sheet image
        image = pygame.image.load(path).convert_alpha()
        # Lists to store normal and flipped frames
        self.sprites =[]
        self.spriteflipped =[]

        # Cut each frame from the sprite sheet
        for position in positions:
            sprite = image.subsurface(pygame.Rect(position))# Extract frame
            sprite= pygame.transform.scale(sprite,(20,20)) # scale it up/ bigger
            self.sprites.append(sprite)
            # Create flipped version
            flipped = pygame.transform.flip(sprite,True,False)
            self.spriteflipped.append(flipped)


    def getSprites(self, flipped):
        # Return flipped frames if facing left, else normal frames
        if flipped== True:
            return self.spriteflipped
        else:
            return self.sprites


