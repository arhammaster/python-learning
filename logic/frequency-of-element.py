array = [20,5,7,3,8,9,7,8,0,3,5,3,2,7,3,9,3,10,36,34]

element_to_find = int(input("Enter the Number to Find Frequency : "))

frequency = 0

for element in array :
    if element_to_find == element :
        frequency += 1

print(frequency)