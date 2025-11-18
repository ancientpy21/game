import pygame
from back import *
GRAVITY = 1             # Rate of downward acceleration
JUMP_STRENGTH = 20       # Initial upward velocity for a jump
FLOOR_Y = HEIGHT*(6/8)


class Player(pygame.sprite.Sprite):
    def __init__(self,badguy_group,background,x=100,y=100):
        #init the sprite
        super.__init__(self)
        # set position and speed
        self.x = x
        self.y = y
        self.badguy_group = badguy_group
        self.background=background
        self.vx = 0
        self.vy = JUMP_STRENGTH
        self.g= 1
        self.jumping = False
        self.on_ground=False
        # upload file
        self.standing = pygame.image.load('assets/asset/white.png').convert_alpha()
        self.jump== pygame.image.load('assets/asset/jump.png').convert_alpha()
        # resize if needed
        self.standing =pygame.transform.scale(self.standing,(60,60))
        self.jump=pygame.transform.scale(self.jump,(60,60))

        self.image=self.standing
        
        self.health_bar = {'ratio': 100}

    def check_boundaries(self):

        # check topright of fish
        if self.rect.top<0:
            self.vy = -self.vy # bounce

        #print(self.background.get_at(self.rect.bottomright))
        front_color = self.background.get_at(self.rect.bottomright)
        if front_color[2]<200: # if not so blue
            self.vy=0
            self.vx =0
            self.rect.bottom = self.rect.bottom -10



    def update(self):
       self.x+=self.vx
       self.y+=self.vy

       #update the rect
       self.rect.center=(self.x,self.y)
        #check boundaries
       self.check_boundaries()

       # collision
       colliding=pygame.sprite.spritecollide(self,self.badguy_group,0)

       if colliding:
           self.health_bar['ratio']-=20
           
           for b in colliding:
               b.x= WIDTH+50
               b.y=FLOOR_Y

                   

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
