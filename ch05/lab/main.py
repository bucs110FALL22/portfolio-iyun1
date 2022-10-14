import pygame

pygame.init()

#variables
screenwidth = 400
screenheight = 300
size = 30
upperlimit = 20
color = "black"
scale = 15
font = pygame.font.Font(None, size)
n = 101
maxvalue = 0
count = 0
iters = {}
maxsofar = 0
maxvalue = 0
pos = (10, 10)

#initialization




for i in range(2, upperlimit + 1):
  #3nPn Sequence
  def sequence(n):
    count = 0
    while True:
        if n == 1:
            break
        elif n % 2 != 0:
            n = n * 3 + 1
            count = count + 1
        elif n % 2 == 0:
            n = n // 2
            count = count + 1
    return count

#checking range
  count = sequence(i*scale)
  print(count)
  iters.update({i*scale: count})
  print(iters)
  sequence(n)

#drawing lines
  screen = pygame.display.set_mode([screenwidth, screenheight])
  screen.fill([0, 255, 0])
  coords = list(iters.items())
    
  if len(coords) > 1:
    pygame.draw.lines(screen, color , False, coords)
    screen.blit(pygame.transform.flip(screen, False, True), (0,0))
  pygame.time.wait(1000)



  if count > maxsofar:
    maxsofar = count
    maxvalue = count
    maxstr = str(maxvalue)
  msg = font.render("The current highest value is:" +maxstr, True, color)
  screen.blit(msg, (0, 0))
  pygame.display.flip()