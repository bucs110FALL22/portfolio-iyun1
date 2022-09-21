import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')
# 3.  Create two turtles



 # 4. Pick up the pen so we don’t get lines

## 5. Your PART A code goes here
#variables
x1=random.randrange(0,20,1)
x2=random.randrange(0,20,1)

michelangelo = turtle.Turtle()
michelangelo.color('orange')
leonardo = turtle.Turtle()
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

#commands
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window = turtle.Screen()
window.bgcolor('lightblue')

for i in (1,3,5,7,9,11,13,15,17,19):
  michelangelo.forward(x1)
for i in (2,4,6,8,10,12,14,16,18,20):
  leonardo.forward(x2)

pygame.time.wait(3000)  

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# PART B - complete part B here
pygame.init()

window=pygame.display.set_mode()
pygame.display.get_surface()
numberofsides=input(int("Please enter number of sides")
#polygoncolor=input("Please enter color of polygon")
polygonpoints=input("Please enter points of polygon as a list")
sidelength=input(int("Please enter length of sides"))
offset=
coords[]

pygame.draw.polygon[surface, polygoncolor, polygonpoints]
print(numberofsides)
print(polygoncolor)
print(polygonpoints)

for i in [numberofsides]
 (2.0 * math.pi * s) / numberofsides
 side_length * math.cos(theta) + offset


window.exitonclick()
