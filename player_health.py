import pygame

class Heathbar():
    def __init__(self,x,y,w,h, max_hp):
        # x and y for green surface
        self.x = x
        self.y = y
        # w and h for red surface
        self.w=w
        self.h=h
        # set parameter for ratio
        self.hp = max_hp
        self.max_hp = max_hp
    
    
    # make surface
    def update(self, life):
        # make a ratio of red and green
        ratio = self.hp/self.max_hp
        pygame.draw.rect(life, 'red', (self.x,self.y,self.w,self.h))
        pygame.draw.rect(life, 'green', (self.x,self.y,self.w*ratio,self.h))




    

  


