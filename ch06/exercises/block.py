class Block:
  def __init__(self):
    self.block_position = (posx, posy) #position of cloud
    self.type = (<block type>) #type of block (i.e. coin block, brick block)
    self.is_broken = False #is the block broken or not