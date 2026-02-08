# List And Tuple

## List

### What is List

List is like a backpack , because it can store a lot of stuff each having its on index's  

### How to create list 

To create a list is to remember to use [ ] instead of ( )

why because ( ) this is Tuple

1. write the list name the = 
2. start it with [
3. put a coma after each index's
4. End it with ]

### Add into List

Use Append

### Removing from list

Use Remove

### Update List Element

List name then the index in [ ] = What you changed it to

### Code Example

The code sort the even numbers in a array and odd in its own

``` py
array = [1,3,4,2,5,6,3,6,7,3,7,4,0,5,6,7,5,2,6,7,8]
```
This stores the numbers

``` py

odd_array = []
even_array = []

```
```py
for element in array :

```
This makes it check all of the index

``` py
    if element != 0 :
        reminder = element % 2

        if reminder == 1:
            odd_array.append(element)            
        elif reminder == 0:
            even_array.append(element)
```
This adds and sorts the index

``` py
print(f"odd array {odd_array}")
print(f"even array {even_array}")
```
Now it prints it

## Tuple 

### What is Tuple

Tuple is like a locked backpack. You can store items inside, but you cannot change anything, but each item still has its own index.

### How to create Tuple

 To create a tuple, you must remember to use ( ) instead of [ ].

1. Write the name then the =
2. Start it with (
3. Put a comma after each index's
4. End it with )

### Removing from Tuple

 You cannot remove from tuple.

### Update Tuple Element

You cannot 

### Code Example

``` py
array = [20,5,7,3,8,9,7,8,0,3,5,3,2,7,3,9,3,10,36,34]

```
This is your array

``` py
array_length = len(array)

biggest_element = 0

for i in range (0,array_length) :
    if biggest_element < array[i] :
        biggest_element = array[i]
```
This checks it

``` py
print (biggest_element)
```
