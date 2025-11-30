import pygame
from back import *

def load_sprite_sheet(path,width,height):
    sheet = pygame.iamge.load(path).convert_alpha()
    sprites =[]

    frames = sheet.get_width() // width
    for i in range(frames):
        frame =pygame.Surface((width,height),pygame.SRCALPHA)

        rect = pygame.Rect(i* width,0,width,height)
        frame.blit(sheet,(0,0), rect)
        sprites.sppend(frame)

    return sprites


