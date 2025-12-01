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
        idleSpritesSheet = SpriteSheet('assets/asset/game file/Main Characters/Mask Dude/Idle (32x32).png',idleSprites)

        jumpSpritesSheet = SpriteSheet('assets/asset/game file/Main Characters/Mask Dude/Jump (32x32).png',jumpSprites)

        fallSpritesSheet = SpriteSheet('assets/asset/game file/Main Characters/Mask Dude/Fall (32x32).png',fallSprites)


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

        ###### MOVEMENT ######
        self.vx,self.vy =0,0
        self.on_ground =False
        self.gravity=GRAVITY

    def input_handle(self):
        keys =pygame.key.get_pressed()
        self.vx= 0

        #----left
        if keys[pygame.K_LEFT]:
            self.vx = -SPEED
            #direction
            self.facing = False
            if self.on_ground:
                self.currentstate = 'IDLE'
        
        #----right
        if keys[pygame.K_RIGHT]:
            self.vx = SPEED
            self.facing = True
            if self.on_ground:
                self.currentstate = 'IDLE'

        #-----jump
        if keys[pygame.K_UP] and self.on_ground:
            self.vy = - JUMP_FORCE
            self.on_ground = False
            self.currentstate= 'JUMP'

    def apply_gravity(self):
        self.vy += self.gravity
        self.y += self.vy

        # Floor collision 
        if self.y >= 600:
            self.y = 600
            self.vy = 0
            self.on_ground = True



    def update(self):
        self.apply_gravity()
        self.input_handle()

        self.selectanimation()
        #position after move
        self.x += self.vx

        # update frame
        frame_index = int(self.animation) % len(self.currentanimation)
        self.image = self.currentanimation[frame_index]
        self.rect.topleft = (self.x, self.y)

        # increase animation timer
        self.animation += self.speed

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

        # update frames (flipped if facing left, FACING =RIGHT)
        self.currentanimation = sheet.getSprites(flipped=not self.facing)