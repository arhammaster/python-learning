number:int =  int (input ("whats your number : "))
 
def loop_with_range(number:int):
    '''
    print all number from 1 to the number 
    '''
    print("print all number from 1 to the ", number)
    for i in range(1, number+1) :
        print (i)

if number > 1 and 50 <= number : 
    print ("invalid number")
else :
    print ("valid number")

    loop_with_range(number)

    # print odd numbers from 1 to number 

    print("print odd numbers from 1 to ", number)
    for i in range (1, number, 2):
        print(i)

    # print even number from 0 to number 

    print("print even numbers from  1 to ",number)
    for i in range (0, number, 2):
        print(i)

    # print number in reverse from number to 1 

    print("print reverse numbers from  1 to ",number)    
    for i in reversed(range(1, number+1)) :
        print(i)

    # print number from 10 to 50 step count by 10 
    print("print number from 10 to 50  step count by 10 ")
    for i in range (10,50,10) :
        print(i)

    # print number from 75 to 5 in reverse step count by 5 

    print("print number from 75 to 5 in reverse step count by 5 ")
    for i in reversed (range(5,75,5)) :
        print(i)

