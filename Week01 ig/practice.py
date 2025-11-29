lehn = (input("Give me a word and ill count how many letters it has : "))
print("Your word has" , (len(lehn)) , "letters")
for E in lehn:
    print(E)
    
height = int(input("What is the height of your triangle : "))

for n in range(height, 0, -1):
    spaces = height - n
    triangle = 2*n -1
    print('' * spaces + '*' * triangle)