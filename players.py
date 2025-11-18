import pygame
from back import *
GRAVITY = 5            # Rate of downward acceleration
JUMP_STRENGTH = 20       # Initial upward velocity for a jump
FLOOR_Y = HEIGHT*(6/8)


class Player(pygame.sprite.Sprite):
    def __init__(self,badguy_group,background,x=100,y=FLOOR_Y):
        #init the sprite
        pygame.sprite.Sprite.__init__(self)
        # set position and speed
        self.x = x
        self.y = y
        
        self.vx = 0
        self.vy = JUMP_STRENGTH
        self.badguy_group = badguy_group
        self.background=background
        
        self.jumping = False
        self.on_ground=False
        self.hp=100
        # upload file
        self.image = pygame.image.load('assets/asset/white.png').convert_alpha()
        
        # resize if needed
        self.image =pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        
        

    def check_boundaries(self):

        # check topright of fish
        if self.rect.top<0:
            self.vy = -self.vy # bounce

        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False



    def update(self):
        self.x+=self.vx
        self.y+=self.vy

        
        #check boundaries
        self.check_boundaries()

         # collision
        colliding=pygame.sprite.spritecollide(self,self.badguy_group,0)

        if colliding:
            self.hp-=20
           
            for b in colliding:
                b.x= WIDTH+50
                b.y=FLOOR_Y
        #sync new position
        self.rect.center = (self.x, self.y)

                   

    def update_event(self):
        
        keys = pygame.key.get_pressed()


        self.vx=0 # reset velocity

        if keys[pygame.K_LEFT]:
            self.vx = -2
        if keys[pygame.K_RIGHT]:
            self.vx = 2


        if keys[pygame.K_UP] and self.on_ground:
            self.jumping= True
            self.vy = -JUMP_STRENGTH

        if self.jumping:
            self.vy += GRAVITY
            if self.vy >0:
                self.jumping= False
                
        
    #draw
    def draw(self,screen):
        screen.blit(self.image,self.rect)
