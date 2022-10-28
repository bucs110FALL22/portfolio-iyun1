class Player:
  def __init__(self):
    self.player_position = (x, y) #position of player
    self.player_num = 1 #player number
    self.player_lives = 3 #number of player lives
    self.is_large = False #state of player's size
    self.running = True
    self.run_images
    self.is_jumping = False

class Block:
  def __init__(self):
    self.block_position = (posx, posy) #position of cloud
    self.type = (<block type>) #type of block (i.e. coin block, brick block)
    self.contents = "1 coin"
    self.is_hit = False #is the block hit or not

class Cloud:
  def __init__(self):
    self.position = (posx, posy) #position of cloud
    self.layer = 0 #layer of cloud (background layer = 0)
    self.quantity = <quantity of clouds next to each other 1-3> #how many clouds are next to each other

class Coin:
  def __init__(self):
    self.coin_position = (posx, posy) #position of coin
    self.coin_value = 1 #value of coin when collects (score increase and coin counter)
    self.is_collected = False #is the coin collected or not

class Goomba:
  def __init__(self):
    self.goomba_position = (posx, posy) #position of goomba
    self.direction = left #direction of goomba travel
    self.is_killed = False #is the goomba dead or not