import pygame
from config import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH+100,y=FLOOR_Y-50,speed=2):
        super().__init__()
        self.x=x
        self.y=y
        self.speed=speed
        self.vx= -self.speed # negative direction
        
        image_path=['enemy/chicken.png','enemy/snail.png','enemy/plant.png']
        
        self.image = pygame.image.load(random.choice(image_path)).convert_alpha()
        self.image= pygame.transform.scale(self.image,(32,32))    
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        

    def update(self):
        self.rect.x -= self.speed

        # Reset when off screen
        if self.rect.right < 0:
            self.rect.left = WIDTH + 50
  