import rectangle

#surface class
class Surface:
#initialize surface method
  def __init__(self, image, xpos, ypos, height, width):
    self.image = image
    self.rect = rectangle.Rectangle(xpos, ypos, height, width)

#get rectangle method
  def getRect(self):
    return self.rect
    
    