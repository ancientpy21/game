from back import *
import pygame
from random import randint

def make_background():
    # make background
    the_land_location='assets\Farmer Story Asset and Backgrounds v2\Farmer Story Backgrounds\Mountains\3 layer Mountains.png'
    the_land= pygame.image.load(the_land_location)

    # get the width and height
    land_width= the_land.get_width()
    land_height= the_land.get_height()

    # make a new surface, background, with the same w,h as screen
    background= pygame.surface((WIDTH,HEIGHT))

    # loop over the background and place the land on it 
    for 




# input background
