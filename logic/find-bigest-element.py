array = [20,5,7,3,8,9,7,8,0,3,5,3,2,7,3,9,3,10,36,34]
array_length = len(array)

biggest_element = 0

for i in range (0,array_length) :
    if biggest_element < array[i] :
        biggest_element = array[i]

print (biggest_element)