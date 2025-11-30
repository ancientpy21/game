import pygame
from config import *
from load_sprite import load_sprite_sheet
GRAVITY = 1            # Rate of downward acceleration
JUMP_STRENGTH = 16      # Initial upward velocity for a jump



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

class Player(pygame.sprite.Sprite):
    ANIMATION_DELAY = 5

  
    def __init__(self, x, y):
        super().__init__()

        self.rect = pygame.Rect(x, y, 32, 32)
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.direction = "right"
        self.animation_count = 0
        self.on_ground = False
        self.jumping = False

        # first sprite
        self.sprite = self.IDLE_RIGHT[0]


    # -------------------- MOVEMENT ----------------------

    def jump(self):
        if self.on_ground:
            self.vy = -JUMP_STRENGTH
            self.jumping = True

    def apply_gravity(self):
        self.vy += GRAVITY
        if self.vy > 20:
            self.vy = 20

    def update_physics(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (self.x, self.y)

        # ground check
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.y = self.rect.y
            self.vy = 0
            self.on_ground = True
            self.jumping = False
        else:
            self.on_ground = False


    # -------------------- INPUT ----------------------

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vx = 0

        if keys[pygame.K_LEFT]:
            self.vx = -4
            self.direction = "left"
        if keys[pygame.K_RIGHT]:
            self.vx = 4
            self.direction = "right"
        if keys[pygame.K_UP]:
            self.jump()


    # -------------------- ANIMATION ----------------------

    def update_animation(self):
        if self.jumping and self.vy < 0:
            action = "jump"
        elif self.vy > 5:
            action = "fall"
        elif self.vx != 0:
            action = "run"
        else:
            action = "idle"

        # pick correct sprite list
        if action == "idle":
            sprites = self.IDLE_RIGHT if self.direction == "right" else self.IDLE_LEFT
        elif action == "run":
            sprites = self.RUN_RIGHT if self.direction == "right" else self.RUN_LEFT
        elif action == "jump":
            sprites = self.JUMP_RIGHT if self.direction == "right" else self.JUMP_LEFT
        else:
            sprites = self.FALL_RIGHT if self.direction == "right" else self.FALL_LEFT

        # animate frames
        index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[index]
        self.animation_count += 1


    # -------------------- UPDATE + DRAW ----------------------

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.update_physics()
        self.update_animation()

    def draw(self, screen, offset_x=0):
        screen.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
