import random
print("Hello i am the turtle guessing game")
tutle = int(input("How many turtles? : "))
wi = int(input("Which turtle will win : "))
if wi == random.randint(2, tutle):
  print("You guessed it right, good boy")
else:
  print("Try again")