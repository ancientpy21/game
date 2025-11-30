import pygame
from load_sprite import load_sprite_sheet
# Player idle file
IDLE_RIGHT = load_sprite_sheet("assets/asset/game file/Main Characters/Mask Dude/Idle (32x32).png", 32, 32)
RUN_RIGHT  = load_sprite_sheet("assets/asset/game file/Main Characters/Mask Dude/Run (32x32).png", 32, 32)
JUMP_RIGHT = load_sprite_sheet("assets/asset/game file/Main Characters/Mask Dude/Jump (32x32).png", 32, 32)
FALL_RIGHT = load_sprite_sheet("assets/asset/game file/Main Characters/Mask Dude/Fall (32x32).png", 32, 32)

# Flip them for left
IDLE_LEFT = [pygame.transform.flip(img, True, False) for img in IDLE_RIGHT]
RUN_LEFT  = [pygame.transform.flip(img, True, False) for img in RUN_RIGHT]
JUMP_LEFT = [pygame.transform.flip(img, True, False) for img in JUMP_RIGHT]
FALL_LEFT = [pygame.transform.flip(img, True, False) for img in FALL_RIGHT]
