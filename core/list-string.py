# 
#  Define a String array with names "Moin, Ajija, Neamat, Arham"
# 
# 
#
#  Output: 
#
#  Moin
#  Ajija
#  Neamat
#  Arham
#

# Define array
names = ("Moin", "Ajija", "Neamat", "Arham")

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

