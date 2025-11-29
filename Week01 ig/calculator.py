print("Hello, i am a calculator")
my_1 = int(input("First number = "))
d = input("operation = ")
my_2 = int(input("Second number = "))
if d == "+":
  print(my_1, d, my_2, "=", my_1 + my_2)
if d == "-":
  print(my_1, d, my_2, "=", my_1 - my_2)
if d == "*":
  print(my_1, d, my_2, "=", my_1 * my_2)
if d == "/":
  print(my_1, d, my_2, "=", my_1 / my_2)
