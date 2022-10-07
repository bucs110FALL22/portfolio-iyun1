import pygame
import random
import math

pygame.init()


#constant variables
Player_1_Score=0
Player_2_Score=0

screen = [300, 300]
x2 = 150
y2 = 150
width = 300
player_selected=False
player_selection=()

#button setup
window = pygame.display.set_mode(screen)
pygame.display.get_window_size()
button_width = 150
button_height = 300
Player_1_hitbox = pygame.Rect(0, 0, button_width, button_height)
Player_2_hitbox = pygame.Rect(150, 0, button_width, button_height)
Player_1_hitbox.topright=Player_2_hitbox.topleft
Player_1_button = pygame.draw.rect(window, "purple", Player_1_hitbox)
Player_2_button = pygame.draw.rect(window, "green", Player_2_hitbox)
pygame.display.flip()


#selecting a player
print("Select a Player by clicking the color you think will win. Left mouse click for Purple, right mouse click for Green.")
mouse_position = pygame.mouse.get_pos()
while not player_selected:
  for event in pygame.event.get():
#    player_selection_side = math.hypot(x1-x2, y1-y2)
#is_in_circle = distance_from_center <= width/2

    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        player_selection = "purple"
        print("You chose purple")
        player_selected = True
      if event.button == 3:
        player_selection = "green"
        print("You chose green")
        player_selected = True
        
#dartboard setup
window.fill("white")
pygame.draw.circle(window, "orange", (150, 150), 150)
pygame.draw.line(window, "black", (150, 0), (150, 300))
pygame.draw.line(window, "black", (0, 150), (300, 150))
pygame.display.flip()

#throwing darts
for i in range(10):
  x1 = random.randrange(0, 301)
  y1 = random.randrange(0, 301)
  pygame.draw.circle(window, "purple", (x1, y1), 5)
  pygame.display.flip()
  pygame.time.wait(300)
  distance_from_center = math.hypot(x1-x2, y1-y2)
  if distance_from_center <= width/2:
    print("Purple hit")
    Player_1_Score=Player_1_Score+1
  else:
    print("Purple miss")
  
  x1 = random.randrange(0, 301)
  y1 = random.randrange(0, 301)
  pygame.draw.circle(window, "green", (x1, y1), 5)
  pygame.display.flip()
  pygame.time.wait(300)
  distance_from_center = math.hypot(x1-x2, y1-y2)
  if distance_from_center <= width/2:
    print("Green hit")
    Player_2_Score = Player_2_Score+1
  else:
    print("Green miss")
print(Player_1_Score)
print(Player_2_Score)

#determining a winner
if Player_1_Score > Player_2_Score:
  print("Purple Wins")
  if player_selection == "purple":
    print("Good Choice")
  else:
    print("Bad Luck, Maybe Next Time")
if Player_1_Score < Player_2_Score:
  print("Green Wins")
  if player_selection == "green":
    print("Good Choice")
  else:
    print("Bad Luck, Maybe Next Time")
if Player_1_Score == Player_2_Score:
  print("It's a tie, what are the odds?")