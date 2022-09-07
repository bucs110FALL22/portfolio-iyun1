import turtle

set_turtle=turtle.Turtle()
set_turtle2=turtle.Turtle()
window=turtle.Screen()
set_turtle.color("purple")
set_turtle.shape("turtle")

set_turtle2.color("red")
set_turtle2.shape("turtle")
set_turtle2.goto(-55, 0)

length=50
angle=90

for i in [angle]*4:
  set_turtle.forward(length)
  set_turtle.left(angle)

for i in [angle]*4:
  set_turtle2.forward(length)
  set_turtle2.left(angle)  

window.exitonclick()