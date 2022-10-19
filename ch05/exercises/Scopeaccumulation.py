def addmultiply(addmultiply1=0, addmultiply2=0):
  result1 = 0
  for i in range(addmultiply2):
    result1 = result1 + addmultiply1 
  return result1

def exponent(number = 0, exp = 0):
  result2 = 1
  for i in range(exp):
    result2 = result2 * number
  return result2

def squarefunc(squareinput = 0):
  result3 = 0
  result3 = exponent(squareinput, 2)
  return result3

def main():
  addmultiply1 = int(input("Please enter a number:"))
  addmultiply2 = int(input("Please enter another number to multiply by the first one:"))
  addmultiplyinput = addmultiply(addmultiply1, addmultiply2)
  print(addmultiplyinput)
  number = int(input("Please enter a number:"))
  exp = int(input("Please enter a number for use as an exponent:"))
  exponentinput = exponent(number, exp)
  print(exponentinput)
  square = int(input("Please enter a number to square:"))
  squareinput = squarefunc(square)
  print(squareinput)

main()