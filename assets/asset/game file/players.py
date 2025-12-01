import pygame
from config import *
from MANAGE import SpriteSheet


idleSprites = [(0,0,32,32),(32,0,32,32),(64,0,32,32),(96,0,32,32),
(128,0,32,32),(160,0,32,32),(192,0,32,32),(224,0,32,32)]
jumpSprites = [(0,0,32,32)]
fallSprites = [(0,0,32,32)]

class Player:
    def __init__(self, position):
    # Load sprite sheets
        self.spriteSheets = {
        'IDLE': SpriteSheet('Main Characters/Mask Dude/Idle (32x32).png', idleSprites),
        'JUMP': SpriteSheet('Main Characters/Mask Dude/Jump (32x32).png', jumpSprites),
        'FALL': SpriteSheet('Main Characters/Mask Dude/Fall (32x32).png', fallSprites)
        }

        self.currentstate = 'IDLE'
        self.animation = 0

        # Fixed horizontal position
        self.x, self.y = position
        self.currentanimation = self.spriteSheets['IDLE'].getSprites()
        self.image = self.currentanimation[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Vertical movement
        self.vy = 0
        self.on_ground = False
        self.gravity = GRAVITY

        # Animation speed
        self.speed = PLAYERIDLE_SPEED

    def input_handle(self):
        keys = pygame.key.get_pressed()
        # Only handle jump
        if keys[pygame.K_UP] and self.on_ground:
            self.vy = -JUMP_FORCE
            self.on_ground = False
            self.currentstate = 'JUMP'

    def apply_gravity(self):
        self.vy += self.gravity
        if self.vy > 20:
            self.vy = 20
        self.rect.y += self.vy

    def vertical_collision(self, tiles):
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                # Only handle landing
                if self.vy > 0:
                    self.rect.bottom = tile.rect.top
                    self.vy = 0
                    self.on_ground = True
                    return
        # If not on any tile
        self.on_ground = False

    def selectanimation(self):
        if not self.on_ground:
            self.currentstate = 'JUMP' if self.vy < 0 else 'FALL'
        else:
            self.currentstate = 'IDLE'  # running in place

        self.speed = PLAYER_SPEED if self.currentstate != 'IDLE' else PLAYERIDLE_SPEED
        self.currentanimation = self.spriteSheets[self.currentstate].getSprites()

    def update(self, tiles):
        self.input_handle()
        self.apply_gravity()
        self.vertical_collision(tiles)
        self.selectanimation()

        # Animation frame update
        frame_index = int(self.animation) % len(self.currentanimation)
        self.image = self.currentanimation[frame_index]
        self.animation += self.speed

        # Keep fixed x
        self.rect.x = self.x
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)