#############################################
# IMPORTS
#############################################
import pygame

#############################################
# PLAYER CLASS
#############################################
class Player(pygame.sprite.Sprite):

    #########################################
    # INITIALIZE SPRITE (runs once)
    #########################################
    def __init__(self, x, y):

        # call sprite constructor
        super().__init__()

        # load image
        self.image = pygame.image.load("assets/player/idle_0.png").convert_alpha()

        # create rectangle based on image size
        self.rect = self.image.get_rect()

        # set starting position
        self.rect.center = (x, y)

        # movement variables
        self.vx = 0          # left / right speed
        self.vy = 0          # vertical speed
        self.on_ground = False

        # animation frames (optional)
        self.anim_idle = [self.image]
        self.anim_index = 0

    #########################################
    # UPDATE (runs every frame)
    #########################################
    def update(self):
        # apply movement
        self.rect.x += self.vx
        self.rect.y += self.vy

        # apply gravity
        self.vy += 1

        # stop falling if touching ground
        if self.rect.bottom >= 600:   # example ground height
            self.rect.bottom = 600
            self.vy = 0
            self.on_ground = True

    #########################################
    # HANDLE INPUT (keys)
    #########################################
    def handle_input(self):
        keys = pygame.key.get_pressed()

        self.vx = 0

        if keys[pygame.K_LEFT]:
            self.vx = -5

        if keys[pygame.K_RIGHT]:
            self.vx = 5

        if keys[pygame.K_UP] and self.on_ground:
            self.vy = -20
            self.on_ground = False

    #########################################
    # DRAW (if not in group)
    #########################################
    def draw(self, screen):
        screen.blit(self.image, self.rect)