# It should take number and print table for it 
# if the number is grater then 100 it should print error message 
# "In valid number, It should be less then 100"

# Example 

# Input 
#   Enter the number : 500
# Output
#   Invalid number, It should be less then 100

# Input 
#   Enter the number : 5
# Output
#   5 X 1 = 5
#   5 X 2 = 10
#   5 X 3 = 15
#   .....
#   5 X 9 = 45
#   5 X 10 = 50


number:int = int(input("Enter number"))
if number >100 :
    print("invalid number,it should be lower then 100 ")
else :
    for i in range (1,12+1) :
        print(number, "X", i, "=", number*i)
  