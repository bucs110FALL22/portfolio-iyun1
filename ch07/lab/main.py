import rectangle
import surface

def main():
#rectangle assertion commands
  r = rectangle.Rectangle(10, 10, 10, 10)
  assert((r.xpos, r.ypos, r.height, r.width) == (10,10,10,10))
  r = rectangle.Rectangle(-1, 1, 1, 1)
  assert((r.xpos, r.ypos, r.height, r.width) == (0,1,1,1))
  r = rectangle.Rectangle(1, -1, 1, 1)
  assert((r.xpos, r.ypos, r.height, r.width) == (1,0,1,1))
  r = rectangle.Rectangle(1, 1, -1, 1)
  assert((r.xpos, r.ypos, r.height, r.width) == (1,1,0,1))
  r = rectangle.Rectangle(1, 1, 1, -1)
  assert((r.xpos, r.ypos, r.height, r.width) == (1,1,1,0))
#surface assertion command
  s = surface.Surface("Test_Image.png", 10, 10, 10, 10)
  assert((s.rect.xpos, s.rect.ypos, s.rect.height, s.rect.width) == (10,10,10,10))
  srect = s.getRect()
  assert(srect.xpos, s.getRect().ypos, srect.height, srect.width) == (10,10,10,10)
  assert s.image 
  print("Test Complete!")

    
main()