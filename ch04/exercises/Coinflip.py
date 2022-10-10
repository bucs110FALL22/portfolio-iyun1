import random
import turtle



#variables
window = turtle.Screen()
my_turtle=turtle.Turtle()
my_turtle.shape("turtle")
window.setup(width=300, height=300, startx=0, starty=0)
turtle.color("black")
coinlist=[1, 2]


outside=False


my_turtle.up()
my_turtle.goto(0,0)

while not outside:
  coin_flip = random.choice(coinlist)
  print(coin_flip)
  POS = []
  POS = my_turtle.pos()
  x=my_turtle.xcor()
  y=my_turtle.ycor()
  if x > 200:
    break
    outside = True
  if x < -200:
    break
    outside = True
  if y < -200:
    break
    outside = True
  if y > 200: 
    break 
    outside = True
  if coin_flip == 1:
    my_turtle.left(90)
    my_turtle.forward(50)
  if coin_flip == 2:
    my_turtle.right(90)
    my_turtle.forward(50)

  
window.exitonclick()