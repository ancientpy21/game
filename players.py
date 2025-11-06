import pygame
from back import *

class Player():
    def __init__(self, x=100, y=500):
        #init the sprite
        pygame.sprite.Sprite.__init__(self)
        # set position and speed
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        # upload file
        self.image = pygame.image.load('assets/asset/white.png').convert_alpha()
        # resize if needed
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # update rect
        self.rect.center = (self.x,self.y)

        # collision if needed

    # event for key control 
    def update_event(self):
        keys = pygame.key.get_pressed()

        self.vx, self.vy = 0, 0  # reset velocity

        if keys[pygame.K_LEFT]:
            self.vx = -2
        if keys[pygame.K_RIGHT]:
            self.vx = 2
        if keys[pygame.K_UP]:
            self.vy = -2
        if keys[pygame.K_DOWN]:
            self.vy = 2

    #draw
    def draw(self,screen):
        screen.blit(self.image,self.rect)
