# Define array with mix number 
# 
# [1,3,4,2,5,6,3,6,7,3,7,4,0,5,6,7,5,2,6,7,8] 
#
# if number is 0 then ignore
# if number is ODD then add into odd_array
# if number is EVEN then add into even_array
# 
# Output should be
# ODD :  [1,3,5,3,7,3,7,5,7,5,7]
# EVEN : [4,2,6,6,4,6,2,6,8] 

array = [1,3,4,2,5,6,3,6,7,3,7,4,0,5,6,7,5,2,6,7,8]
odd_array = []
even_array = []
for element in array :
    
    if element != 0 :
        reminder = element % 2

        if reminder == 1:
            odd_array.append(element)            
        elif reminder == 0:
            even_array.append(element)

print(f"odd array {odd_array}")
print(f"even array {even_array}")