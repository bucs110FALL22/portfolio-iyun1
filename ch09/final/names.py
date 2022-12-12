from randomquantity import RandomQuantity
import requests
import json

class Names(object):
  def __init__(self):
      '''Setting up random names API'''
      pass
  def __str__(self):
    name_url = "https://randomuser.me/api/?inc=name&noinfo"
    return name_url
  def get_names(self):
    '''Generates a list of random names'''
    '''Quantity of names generated is determined by RandomQuantity class'''
    '''Returns a randomly genereated list of names'''
    name_url = "https://randomuser.me/api/?inc=name&noinfo"
    name_quantity = RandomQuantity.get_quantity(0)
    name_list = []
    for get in range(name_quantity):
      getnames = requests.get(name_url).json()
      first_names = getnames["results"][0]["name"]["first"]
      name_list.append(first_names)
    return name_list
