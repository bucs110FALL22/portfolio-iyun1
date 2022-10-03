import random
import turtle

#   Write a program that behaves in the following way:
# A turtle begins in the center of the screen.
# Flip a coin. 
# heads: turn to the left 90 degrees. 
# tails: turn to the right 90 degrees.
# Take 50 steps forward.
# If the turtle has moved outside the screen the program stops, otherwise go back to step 2 and repeat

#A few hints:
# get the turtle moving randomly around the screen first
# Get the turtle's coordinates to calculate if the turtle is visible on screen
# You will need to use a while loop
# the condition should be based on whether the turtle is visible on the screen or not 
# Use the random library to simulate flipping a coin (50/50 odds)
# Use an if statement to determine the direction the turtle should turn
# move forward
# calculate if the turtle's position is on screen again

my_turtle=turtle.Turtle()

my_turtle.shape("turtle")

outside=False
while not outside
coin_flip=random.randrange(0, 2, 1)
if coin_flip==1:
  turtle.left(90)
  coin_flip="heads"
else:
  turtle.right(90)
  coin_flip="tails"

