class Rectangle:
#initialize rectangle method  
  def __init__(self, xpos = 0, ypos = 0, height = 3, width = 4):
    self.xpos = xpos
    self.ypos = ypos
    self.height = height
    self.width = width
    #0 correct statements
    if self.xpos <0:
      self.xpos = 0
    if self.ypos < 0:
      self.ypos = 0
    if self.height < 0:
      self.height = 0
    if self.width < 0:
      self.width = 0
  def getRect(self):
    return 

#self method  
  def __str__(self):
    s = "(xpos: {}, ypos: {}) width: {}, height: {}".format(self.xpos, self.ypos, self.width, self.height)
    return s