x = int(input("Enter the starting number (x): "))
y = int(input("Enter the ending number (y): "))
start = 0
end = 0
sum = 0
if x < y:
    start = x
    end = y
else:
    start = y
    end = x
for i in range (start, end + 1):
    sum += i
    print("i =", i, "sum =", sum)
print("Sum of numbers from", x, "to", y, "is", sum)
