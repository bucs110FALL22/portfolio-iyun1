class Coin:
  def __init__(self):
    self.coin_position = (posx, posy) #position of coin
    self.coin_value = 1 #value of coin when collects (score increase and coin counter)
    self.is_collected = False #is the coin collected or not