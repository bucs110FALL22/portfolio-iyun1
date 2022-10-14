import turtle

myturtle=turtle.Turtle()
myturtle.color("green")
myturtle.shape("turtle")
def drawEQshape(myturtle = None, side_length = 0, number_of_sides=0, angle = 0):
  for i in number_of_sides * [360/number_of_sides]:
    myturtle.forward(side_length)
    myturtle.left(i)


number_of_sides = int(input("Enter number of sides:"))
side_length = int(input("Enter side length:"))
angle = int(input("Enter angle:"))
drawEQshape(myturtle, side_length, number_of_sides, angle)