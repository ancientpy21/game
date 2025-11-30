import pygame
from config import *
from MANAGE import SpriteSheet

idleSprites = [
    (0, 0, 32, 32),
    (32, 0, 32, 32),
    (64, 0, 32, 32),
    (96, 0, 32, 32),
    (128, 0, 32, 32),
    (160, 0, 32, 32),
    (192, 0, 32, 32),
    (224, 0, 32, 32)
]
jumpSprites = [
    (0, 0, 32, 32)
]
fallSprites = [
    (0, 0, 32, 32)
]

class Player():
    def __init__(self,position, facing):
        #load spritesheet
        idleSpritesSheet = SpriteSheet(SPRITESHEET_PATH + 'Main Characters/Mask Dude/Idle (32x32).png', idleSprites)
        jumpSpritesSheet = SpriteSheet(SPRITESHEET_PATH + 'Main Characters/Mask Dude/Jump (32x32).png', jumpSprites)
        fallSpritesSheet = SpriteSheet(SPRITESHEET_PATH + 'Main Characters/Mask Dude/Fall (32x32).png', fallSprites)

        #make simpler by creating dictionary
        self.spriteSheets ={
            'IDLE': idleSpritesSheet,
            'JUMP': jumpSpritesSheet,
            'FALL': fallSpritesSheet
        }
        #initialize variable in sprite animation
        self.facing = facing
        self.currentstate = 'IDLE'
        self.animation =0
        self.x,self.y=position
        self.speed =  PLAYERIDLE_SPEED

        # Create a default rect to avoid crashes before update()
        self.currentanimation = self.spriteSheets["IDLE"].getSprites(flipped=not facing)
        self.image = self.currentanimation[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.selectanimation()

        # update frame
        self.image = self.currentanimation[int(self.animation)]
        self.rect.topleft = (self.x, self.y)

        # increase animation timer
        self.animation += self.speed

        # loop animation
        if self.animation >= len(self.currentanimation):
            self.animation = 0

    #DRAW
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # CHOSE ANIMATION
    def selectanimation(self):
        # select correct speed
        if self.currentstate == "IDLE":
            self.speed = PLAYERIDLE_SPEED
        else:
            self.speed = PLAYER_SPEED

        # load correct sprite sheet
        sheet = self.spriteSheets[self.currentstate]

        # update frames (flipped if facing left)
        self.currentanimation = sheet.getSprites(flipped=not self.facing)