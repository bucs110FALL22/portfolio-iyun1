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

window.exitonclick()
# PART B - complete part B here
pygame.init()

coords=[]
num_sides=3
side_length=10
offset=50

pygame.Surface()
window=pygame.display.set_mode()


for i in range(num_sides):
  theta = (2.0 * math.pi*i) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  points=(x,y)

pygame.draw.polygon('black', (25, 50),(50,0),(0,0))
window.display.flip
pygame.time.wait(3000)
window.fill

