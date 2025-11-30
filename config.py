import pygame
from load_sprite import load_sprite_sheet

#this is where the background shape
WIDTH = 1000
HEIGHT = 600

# frames
FPS = 60
# Player movement
GRAVITY = 0.8
PLAYER_SPEED = 5
JUMP_FORCE = 15
DELAY =5 

# Terrain & blocks
BLOCK_SIZE = 50
TILE = 32
# Player idle file
IDLE_RIGHT = load_sprite_sheet("assets/Player/idle.png", 32, 32)
RUN_RIGHT  = load_sprite_sheet("assets/Player/run.png", 32, 32)
JUMP_RIGHT = load_sprite_sheet("assets/Player/jump.png", 32, 32)
FALL_RIGHT = load_sprite_sheet("assets/Player/fall.png", 32, 32)

# Flip them for left
IDLE_LEFT = [pygame.transform.flip(img, True, False) for img in IDLE_RIGHT]
RUN_LEFT  = [pygame.transform.flip(img, True, False) for img in RUN_RIGHT]
JUMP_LEFT = [pygame.transform.flip(img, True, False) for img in JUMP_RIGHT]
FALL_LEFT = [pygame.transform.flip(img, True, False) for img in FALL_RIGHT]