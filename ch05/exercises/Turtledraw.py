import turtle

myturtle=turtle.Turtle()
myturtle.color("green")

def drawEQshape(myturtle = None, side_length = 0, ns=0):
  for i in range(ns):
    myturtle.forward(side_length)
    myturtle.left(90)


number_of_sides = int(input("Enter number of sides:"))
side_length = int(input("Enter side length:"))
drawEQshape(myturtle, side_length, number_of_sides)