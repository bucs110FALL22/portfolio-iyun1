import requests

class RandomQuantity(object):
  def __init__(self):
    '''Sets up random number API'''  
    pass
  def __str__(self):
    quantity_url = "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1"
    return quantity_url
  def get_quantity(self, name_quantity = 0):
    '''Generates a random number from 1 to 10'''
    '''Used to determine a quantity of names to generate'''
    '''Returns an randomly generated integer'''
    quantity_url = "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1"
    getquantity = requests.get(quantity_url).json()
    for num in getquantity:
      name_quantity = num
    return name_quantity