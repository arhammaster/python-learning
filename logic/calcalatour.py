def add(a, b):      
    print("Result:", a + b)

def subtract(a, b): 
    print("Result:", a - b)

def multiply(a, b): 
    print("Result:", a * b)

def divide(a, b):
    if b != 0: print("Result:", a / b)
    else:      print("Error! Can't divide by zero.")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

choice = input("Enter math symbol (+, -, *, /): ")

if choice == "+":
    add(x, y)
elif choice == "-":
    subtract(x, y)
elif choice == "*":
    multiply(x, y)
elif choice == "/":
    divide(x, y)
else:
    print("Invalid symbol!")

    