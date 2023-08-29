import pygame
import math
from random import *
import time
import numpy as np


pygame.init()

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

display_width = 600
display_height = 250
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fourier Series")
x0,y0 = (display_width/4),(display_height/2)
gameDisplay.fill(white)

graph = []
graphstart = int(display_width/2)
theta = 0

circleAmt = int(input("How many circles do you want: "))

circle = []

while circleAmt >= 1:
	circleAmt = circleAmt - 1
	circleRadius = int(input("What do you want the circle radius to be: "))
	cirlceFrequency = int(input("What do you want the circle radius to be: "))

	circle.append([circleRadius, cirlceFrequency])
	
	gameDisplay.fill(white)

	centre = [x0,y0]
	
print(circle)

for entry in circle:
	print("a")
	
	