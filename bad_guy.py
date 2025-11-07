import pygame
from back import *
from random import randint


class Badguy(pygame.sprite.Sprite):
    def __init__(self): #, player
        pygame.sprite.Sprite.__init__(self)
        self.vx= randint(-3,-1)
        self.vy= 0
        self.x=WIDTH + 100
        self.y=HEIGHT*(6/8)
        self.image= pygame.image.load('assets/asset/goblin.png').convert_alpha()
        self.image= pygame.transform.flip(self.image,1,0)
        self.image= pygame.transform.scale(self.image,(80,80))
        #self.target=player
        self.rect=self.image.get_rect()
        #self.speed= randint(1,3)
        
    def update(self):
        # update position
        self.x += self.vx
        self.y = HEIGHT*(3/4)

        # update the rect
        self.rect.center = (self.x,self.y)

        # update speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

