import random

# Variables

RNG=random.randrange(1, 11)
guessinput=range(1, 11, 1)
for i in [3,2,1]
  
#Commands
guess=int(input("Guess a random a number between 1 and 10:"))


if guess==RNG:
    print("Correct")
  
if guess<RNG:
    print("Too low, you have", remainingchances, "left.")
if guess>RNG:
    print("Too high, you have", remainingchances, "left.")

