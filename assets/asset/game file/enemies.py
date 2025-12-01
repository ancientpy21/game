import pygame
from config import *
import random


class Enemy(pygame.sprite.Group):
    def __init__(self,x=WIDTH+100,y=FLOOR_Y-50,image_path=None,speed=2):
        super().__init__()
        self.x=x
        self.y=y
        self.speed=speed
        self.vx= -self.speed # negative direction
        
        if image_path is None:
            image_path=['enemy/chicken.png','enemy/snail.png','enemy/wood.png']
        
        self.image = pygame.image.load(random.choice(image_path)).convert_alpha()    
        self.rect = self.image.get_rect(topleft=(x, y))
        

    def update(self):
        self.rect.x += self.vx
        self.x+=self.rect.x
        if self.rect.bottom>= self.floor_y:
            self.rect.bottom =self.floor_y

        if self.x >0:
            self.x= WIDTH + 100
    
    def draw(self, screen): 
        screen.blit(self.image, self.rect)