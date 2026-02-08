import random

how_many_Digits = 7
starting_number = 1
ending_number = 50

def generate_number(digits, start, end):
    number_chain = "-"
    for i in range(digits):
        next_number = random.randint(start, end);
        block = "-" + str(next_number) + "-"
        if(block not in number_chain) :
            number_chain += str(next_number) + "-"
        else : 
            i -= 1
    return number_chain

for i in range (10) :
    print(generate_number(how_many_Digits, starting_number, ending_number))

