import random
dice = random.randint(1, 6)

while True:
    guess = int(input("Guess number between 1 to 6 : "))
    if guess == dice:
     break
    elif guess > dice:
         print("less than the number")
    else:
        print("more than the number")
print("GOOD BOY")