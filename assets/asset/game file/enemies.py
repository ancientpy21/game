import pygame
from config import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH+100,y=FLOOR_Y,speed=1):
        super().__init__()
        self.x=x
        self.y=y
        self.speed=speed
        self.vx= -self.speed # negative direction
        
        image_path=['enemy/chicken.png','enemy/snail.png','enemy/plant.png']
        
        self.image = pygame.image.load(random.choice(image_path)).convert_alpha()
        self.image= pygame.transform.scale(self.image,(32,32))    
        self.rect = self.image.get_rect()
        self.rect.x = x if x is not None else WIDTH + random.randint(50, 300)
        
        self.rect.bottom = y if y is not None else FLOOR_Y - random.randint(0, 10)
        

    def update(self):
        self.rect.x -= self.speed

        # Reset when off screen
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(50, 300)  
            self.rect.bottom = FLOOR_Y - random.randint(0, 10)

  