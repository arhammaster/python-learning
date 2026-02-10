# 
#  Define a String array with names "Jack, Jill, Sarah, Arjun"
# 
# 
#
#  Output: 
#
#  Jack
#  Jill
#  Sarah
#  Arjun
#

# Define array
names = ("Jack", "Jill", "Sarah", "Arjun")

# print array without loop
print(names)

#print array element
print(names[1])

# print Array by index
print("print array with for loop with i pointer ")
array_name_length = len(names)
for i in range (array_name_length) :
    print(names[i])

# print array by element
print("print array with for each loop")
for name in names : 
    print (name)

