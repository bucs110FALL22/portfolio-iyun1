class Rectangle:
  def__init__(self, xpos, ypos, width, height):
    self.xpos = (0, 0)
    self.ypos = (0, 0)
    self.width = 4
    self.height = 3
  getRect(self)

#self method  
  def __str__(self):
    s = "(xpos: {}, ypos: {}) width: {}, height: {}".format(self.xpos, self.ypos, self.width, self.height)
    return s