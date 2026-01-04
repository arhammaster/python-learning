# Def

Def is a keyword that defines a function or creates a function.

##  Why do we use Def ?

### Def is used for 3 reasons

  -  avoid code **repetition** .
  -  **origination** so it keep code in small block instead rewriting it.
  -  **simple understanding** instead of reading a lot of code you could just read the block


## Example 
 
 A function definition that prints hello world

```py
 def hello_world():
    print("hello world")
```

Calling hello world function 

```py
hello_world()

hello world
```
Then it prints hello world.

## Input parameter into def    

Input parameter into def is

## Return output from the def 

**Return keyword is used to exit a function and return a value**

## How do you use return with Def

### There are a few main reasons

we use return instead of print because print shows it then it forgets about it but return stores it.
 

### The Difference: print vs. return

#### Where does it go?

print value  : To the Screen.

return value: To a Variable.

#### Can you use it later?

print value : No. It is just a showing it for you to look at.

return value: Yes. It the computer save the data.

#### Program Flow

print value: The function does a job and tells you about it.

return value: The function does a job and hands you the result.

## Example when you use print

```py

def add_return(a, b):
    print (a + b)
```
you can see the answer

After the next line crashes

```py

total = add_return(5, 5)
 
print(total + 20) 

```
Now it show error because it tries nothing + 20

## Example when we use return
```py

def add_return(a, b):
    return a + b

```
now it holds the number 10

```py

total = add_return(5, 5)

```
now you can use it for more math

```py

print(total + 20) 

```
now the result is 30

 