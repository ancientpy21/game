import pygame
from config import *
from MANAGE import SpriteSheet


# Define sprite coordinates for the SpriteSheet class
idleSprites = [(0,0,32,32),(32,0,32,32),(64,0,32,32),(96,0,32,32),
(128,0,32,32),(160,0,32,32),(192,0,32,32),(224,0,32,32)]
jumpSprites = [(0,0,32,32)]
fallSprites = [(0,0,32,32)]


class Player:
    def __init__(self, x, y):
        # Load sprite sheets for IDLE, JUMP, FALL states
        self.spriteSheets = {
            'IDLE': SpriteSheet('Main Characters/Mask Dude/Idle (32x32).png', idleSprites),
            'JUMP': SpriteSheet('Main Characters/Mask Dude/Jump (32x32).png', jumpSprites),
            'FALL': SpriteSheet('Main Characters/Mask Dude/Fall (32x32).png', fallSprites)
        }
        self.currentstate = 'IDLE'
        self.animation = 0
        self.x = x 
        self.y = y 
        self.facing_left = False  # Added for flipping sprites
        
        # Initial image and rect setup
        self.currentanimation = self.spriteSheets['IDLE'].getSprites(self.facing_left)
        self.image = self.currentanimation[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Physics/Movement variables
        self.vy = 0
        self.on_ground = True
        self.gravity = GRAVITY
        self.floor_y = FLOOR_Y# Fixed floor height from config
        self.speed = PLAYERIDLE_SPEED

    def input_handle(self):
        keys = pygame.key.get_pressed()
        
        # Handle Jump
        if keys[pygame.K_UP] and self.on_ground:
            self.vy = -JUMP_FORCE
            self.on_ground = False
            self.currentstate = 'JUMP'

        # Handle facing direction (even if fixed X)
        if keys[pygame.K_LEFT]:
            self.facing_left = True
        elif keys[pygame.K_RIGHT]:
            self.facing_left = False

    def apply_gravity(self):
        # Increase vertical velocity and cap it
        self.vy += self.gravity
        if self.vy > 20:
            self.vy = 20
        self.rect.y += self.vy

    def floor_collision(self):
        # Check collision with fixed floor
        if self.rect.bottom >= self.floor_y:
            # Snap to floor, reset velocity, set on_ground
            self.rect.bottom = self.floor_y
            self.vy = 0
            self.on_ground = True

    def selectanimation(self):
        # Determine state (JUMP, FALL, IDLE)
        if not self.on_ground:
            self.currentstate = 'JUMP' if self.vy < 0 else 'FALL'
        else:
            self.currentstate = 'IDLE'

        # Set speed
        self.speed = PLAYER_SPEED if self.currentstate != 'IDLE' else PLAYERIDLE_SPEED

    def update(self):
        self.input_handle()
        self.apply_gravity()
        self.floor_collision() 
        self.selectanimation()

        # Update current animation based on state AND facing direction
        current_sheet = self.spriteSheets[self.currentstate]
        self.currentanimation = current_sheet.getSprites(self.facing_left)

        # Update image frame
        frame_index = int(self.animation) % len(self.currentanimation)
        self.image = self.currentanimation[frame_index]
        self.animation += self.speed

        # Maintain fixed x position and update internal position variables
        self.rect.x = self.x
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self, screen):
        # Draw player to screen
        screen.blit(self.image, self.rect)