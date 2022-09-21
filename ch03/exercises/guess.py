import random

# Variables

RNG=random.randrange(1, 11)
guessinput=range(1, 11, 1)
guess=int(input("Guess a random a number between 1 and 10:"))
numguesses=1

#Commands
print(guess)
for i in range(3):
  if guess < RNG:
    print("Too low, try again:", guess)
  if guess > RNG:
    print("Too high, try again:", guess)
  if guess==RNG:
    print("Correct")
    break
