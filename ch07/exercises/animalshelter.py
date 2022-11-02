import time

class Animalshelter:
  def __init__(self, name = None,  type = None):
    self.name = name
    self.date_arrive = time.strftime("%m/%d/%Y")
    self.id = time.strftime("%d%m%M%S")
    #self.id = self(id)
    #self.id = uuid()
    self.date_adopted = None

  def setadopted(self):
    self.date_adopted = time.strftime("%m/%d/%Y")

  def __str__():
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\ndate_arrive: {self.date_arrived}"
    result_str += f"\ndate_adopted: {self.date_adopted}"
    return result_str

def main():
  name = input("Please enter name of animal: ")
  type = input("Please enter type of animal: ")
  fido = Animal(name, type)
  fido.setAdopted()
main()

