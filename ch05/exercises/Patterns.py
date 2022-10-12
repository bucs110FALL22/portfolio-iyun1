def starpyramid():
  starlevel=int(input("How many levels do you want your pyramid to have?"))
  

  
  for i in range(1,starlevel +1):  
  
    print(i * "*")
    

starpyramid()

def starminus():
  starlevel=int(input("How many levels do you want your pyramid to have?"))
  starcount = 1

  
  for i in range(starlevel, 0, -1):  
  
    print(i * "*" )
    
starminus()
