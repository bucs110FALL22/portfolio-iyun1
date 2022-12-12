from names import Names
from randomquantity import RandomQuantity
 

def NamesProxy(name_quantity=None):
  '''Calls the random quantity and random names methods'''
  '''Displays a list of random names and the quantity of random names generated'''
  name_list_results = Names.get_names(0)
  name_quantity = len(name_list_results)
  print("Quantity of Names Generated:", name_quantity)
  print("Random Name(s) Generated:", name_list_results)
  return name_quantity

 