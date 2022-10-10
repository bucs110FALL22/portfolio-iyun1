def starpyramid():
  starlevel=int(input("How many levels do you want your pyramid to have?"))
  

  
  for i in range(starlevel):  
  
    print((i+1) * "*")
    

starpyramid()

def starminus():
  starlevel=int(input("How many levels do you want your pyramid to have?"))
  starcount = 1

  
  for i in range(starlevel+1):  
  
    print((starlevel * "*" ))
    starlevel = starlevel - 1
starminus()
