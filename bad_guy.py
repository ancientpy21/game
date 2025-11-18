import pygame
from back import *
from random import randint, choice


class Badguy(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.vx= -5
        self.vy= 0
        self.x=WIDTH+100
        self.y=HEIGHT*6/8
        self.assets= ['assets/asset/goblin.png',
                      'assets/asset/result_0.png',
                      'assets/asset/green.png']
        self.fp= choice(self.assets)
        self.image= pygame.image.load(self.fp)
        #flip the fish
        self.image= pygame.transform.flip(self.image,1,0)
        self.image= pygame.transform.scale(self.image,(80,80))
        #self.target=player
        self.rect=self.image.get_rect()
       
        self.speed= randint(1,3)
        self.player=player
        self.state='alive'
    def update(self):
        # update position
        self.x += self.vx
        self.y = HEIGHT*(3/4)
        
        # update the rect
        self.rect.center = (self.x,self.y)
        # update position
        if self.rect.right<0:
            self.x=WIDTH+50

        # update speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

