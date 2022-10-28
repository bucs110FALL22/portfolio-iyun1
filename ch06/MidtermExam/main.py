import turtle

#house build proposal functions

#house build proposal
def house_build_proposal(answer = None):
  if answer == "Y":
    print("Great! Let's get started.")
    base_proposal_input = input("Would you like to draw a base? Y/N:")
    answer = base_proposal_input
    return answer
  elif answer == "y":
    print("Great! Let's get started.")
    base_proposal_input = input("Would you like to draw a base? Y/N:")
    answer = base_proposal_input
    return answer
  elif answer == "N":
    print("Then this program won't be of much use to you.")
  elif answer == "n":
    print("Then this program won't be of much use to you.")
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")

#base drawing proposal
def draw_base_proposal(answer = None):
  if answer == "Y":
    base_color_input = input("Please enter the color you would like your house's base to be:")
    draw_turtle_base(base_color_input)
    roof_proposal_input = input("Would you like to draw a roof? Y/N:")
    answer =  roof_proposal_input
    return answer
  elif answer == "y":
    base_color_input = input("Please enter the color you would like your house's base to be:")
    draw_turtle_base(base_color_input)
    roof_proposal_input = input("Would you like to draw a roof? Y/N:")
    answer = roof_proposal_input
    return answer
  elif answer == "N":
    roof_proposal_input = input("Would you like to draw a roof? Y/N:")
    answer = roof_proposal_input
    return answer
  elif answer == "n":
    roof_proposal_input = input("Would you like to draw a roof? Y/N:")
    answer = roof_proposal_input
    return answer
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")  

#roof draw proposal
def draw_roof_proposal(answer = None):
  if answer == "Y":
    roof_color_input = input("Please enter the color you would like your house's roof to be:")
    draw_turtle_roof(roof_color_input)
    upper_windows_proposal_input = input("Would you like to draw upper windows? Y/N:")
    answer = upper_windows_proposal_input
    return answer
  elif answer == "y":
    roof_color_input = input("Please enter the color you would like your house's roof to be:")
    draw_turtle_roof(roof_color_input)
    upper_windows_proposal_input = input("Would you like to draw upper windows? Y/N:")
    answer = upper_windows_proposal_input
    return answer
  elif answer == "N":
    upper_windows_proposal_input = input("Would you like to draw upper windows? Y/N:")
    answer = upper_windows_proposal_input
    return answer
  elif answer == "n":
    upper_windows_proposal_input = input("Would you like to draw upper windows? Y/N:")
    answer = upper_windows_proposal_input
    return answer
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")
    
#draw upper windows proposal
def draw_upper_windows_proposal(answer = None):
  if answer == "Y":
    upper_windows_color_input = input("Please enter the color you would like your upper windows to be:")
    draw_turtle_upper_windows(upper_windows_color_input)
    draw_lower_windows_input = input("Would you like to draw lower windows? Y/N:")
    answer = draw_lower_windows_input
    return answer
  elif answer == "y":
    upper_windows_color_input = input("Please enter the color you would like your upper windows to be:")
    draw_turtle_upper_windows(upper_windows_color_input)
    draw_lower_windows_input = input("Would you like to draw lower windows? Y/N:")
    answer = draw_lower_windows_input
    return answer
  elif answer == "N":
    draw_lower_windows_input = input("Would you like to draw lower windows? Y/N:")
    answer = draw_lower_windows_input
    return answer
  elif answer == "n":
    draw_lower_windows_input = input("Would you like to draw lower windows? Y/N:")
    answer = draw_lower_windows_input
    return answer
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")

#draw lower windows proposal
def draw_lower_windows_proposal(answer = None):
  if answer == "Y":
    lower_windows_color_input = input("Please enter the color you would like your house's lower windows to be:")
    draw_turtle_lower_windows(lower_windows_color_input)
    door_proposal_input = input("Would you like to draw a door? Y/N:")
    answer = door_proposal_input
    return answer
  elif answer == "y":
    lower_windows_color_input = input("Please enter the color you would like your house's lower windows to be:")
    draw_turtle_lower_windows(lower_windows_color_input)
    door_proposal_input = input("Would you like to draw a door? Y/N:")
    answer = door_proposal_input
    return answer
  elif answer == "N":
    door_proposal_input = input("Would you like to draw a door? Y/N:")
    answer = door_proposal_input
    return answer
  elif answer == "n":
    door_proposal_input = input("Would you like to draw a door? Y/N:")
    answer = door_proposal_input
    return answer
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")

#draw door proposal
def draw_door_proposal(answer = None):
  if answer == "Y":
    door_color_input = input("Please enter the color you would like your house's door to be:")
    draw_turtle_door(door_color_input)
    doorknob_proposal_input = input("Would you like to draw a doorknob? Y/N:")
    answer = doorknob_proposal_input
    return answer
  elif answer == "y":
    door_color_input = input("Please enter the color you would like your house's door to be:")
    draw_turtle_door(door_color_input)
    doorknob_proposal_input = input("Would you like to draw a doorknob? Y/N:")
    answer = doorknob_proposal_input
    return answer
  elif answer == "N":
    doorknob_proposal_input = input("Would you like to draw a doorknob? Y/N:")
    answer = doorknob_proposal_input
    return answer
  elif answer == "n":
    doorknob_proposal_input = input("Would you like to draw a doorknob? Y/N:")
    answer = doorknob_proposal_input
    return answer
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")

#draw doorknob proposal
def draw_doorknob_proposal(answer = None):
  if answer == "Y":
    doorknob_color_input = input("Please enter the color you would like your house's doorknob to be:")
    draw_turtle_doorknob(doorknob_color_input)
    print("Congragulations! Your house is now complete (at least, as complete as you decided to make it).")
  elif answer == "y":
    doorknob_color_input = input("Please enter the color you would like your house's doorknob to be:")
    draw_turtle_doorknob(doorknob_color_input)
    print("Congragulations! Your house is now complete (at least, as complete as you decided to make it).")
  elif answer == "N":
    print("Congragulations! Your house is now complete (at least, as complete as you decided to make it).")
  elif answer == "n":
    print("Congragulations! Your house is now complete (at least, as complete as you decided to make it).")
  elif answer!= "Y" or "y" or "N" or "n":
    print("Invalid response. Please enter ""Y"" for Yes or ""N ""for no.")

#turtle draw house functions

#drawing house base
def draw_turtle_base(draw_base_color=None):
    draw_turtle_base = turtle.Turtle()
    draw_turtle_base.color(draw_base_color)
    draw_turtle_base.up()
    draw_turtle_base.goto(-55, -70)
    draw_turtle_base.down()
    for i in range(4):
        draw_turtle_base.forward(100)
        draw_turtle_base.left(90)
    draw_turtle_base.hideturtle()

    #drawing house roof
def draw_turtle_roof(draw_roof_color=None):
    draw_turtle_roof = turtle.Turtle()
    draw_turtle_roof.color(draw_roof_color)
    draw_turtle_roof.up()
    draw_turtle_roof.goto(-55, 30)
    draw_turtle_roof.left(90)
    draw_turtle_roof.down()
    for i in range(2):
      draw_turtle_roof.right(60)
      draw_turtle_roof.forward(58)
    draw_turtle_roof.hideturtle()

    #drawing house upper windows
def draw_turtle_upper_windows(draw_upper_windows_color = None):
    draw_turtle_upper_windows = turtle.Turtle()
    draw_turtle_upper_windows.color(draw_upper_windows_color)
    draw_turtle_upper_windows.up()
    draw_turtle_upper_windows.goto(-5, 0)
    draw_turtle_upper_windows.down()
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(25)
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(35)
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(25)
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(70)
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(25)
    draw_turtle_upper_windows.left(90)
    draw_turtle_upper_windows.forward(35)
    draw_turtle_upper_windows.hideturtle()

    #drawing house lower windows
def draw_turtle_lower_windows(draw_lower_windows_color = None):
    draw_turtle_lower_windows = turtle.Turtle()
    draw_turtle_lower_windows.color(draw_lower_windows_color)
    draw_turtle_lower_windows.up()
    draw_turtle_lower_windows.goto(-40, -60)
    draw_turtle_lower_windows.down()
    for i in range(8):
      draw_turtle_lower_windows.forward(10)
      draw_turtle_lower_windows.left(45)
    draw_turtle_lower_windows.up()
    draw_turtle_lower_windows.goto(20, -60)
    draw_turtle_lower_windows.down()
    for i in range(8):
      draw_turtle_lower_windows.forward(10)
      draw_turtle_lower_windows.left(45)
    draw_turtle_lower_windows.hideturtle()
       
    #drawing house door
def draw_turtle_door(draw_door_color = None):
    draw_turtle_door = turtle.Turtle()
    draw_turtle_door.color(draw_door_color)
    draw_turtle_door.up()
    draw_turtle_door.goto(-15, -70)
    draw_turtle_door.down()
    for i in range(2):
        draw_turtle_door.forward(20)
        draw_turtle_door.left(90)
        draw_turtle_door.forward(30)
        draw_turtle_door.left(90)
    draw_turtle_door.hideturtle()

    #drawing doorknob
def draw_turtle_doorknob(draw_doorknob_color = None):
    draw_turtle_doorknob = turtle.Turtle()
    draw_turtle_doorknob.color(draw_doorknob_color)
    draw_turtle_doorknob.up()
    draw_turtle_doorknob.goto(-13, -60)
    draw_turtle_doorknob.down()
    draw_turtle_doorknob.right(90)
    for i in range(360):
        draw_turtle_doorknob.forward(.02)
        draw_turtle_doorknob.left(1)
    draw_turtle_doorknob.hideturtle()


def main():
  house_proposal_input = input("Would you like to draw a house? Y/N:")
  house_proposal_answer = house_build_proposal(house_proposal_input)
  draw_base_answer = draw_base_proposal(house_proposal_answer)
  draw_roof_answer = draw_roof_proposal(draw_base_answer)
  draw_upper_windows_answer = draw_upper_windows_proposal(draw_roof_answer)
  draw_lower_windows_answer = draw_lower_windows_proposal(draw_upper_windows_answer)
  draw_door_answer = draw_door_proposal(draw_lower_windows_answer)
  draw_doorknob_answer = draw_doorknob_proposal(draw_door_answer)
  
main()
