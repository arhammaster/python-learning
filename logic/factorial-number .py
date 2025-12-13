number = int(input("Enter a number : "))
factorial = 1
for i in range (2, number + 1):
     factorial = factorial * i
     print ("i =", i, "factorial =", factorial)
print("Factorial of", number, "is", factorial)