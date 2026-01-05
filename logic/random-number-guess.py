import random

how_many_Digits = int(input("Enter number of digits that your number chain will be longer: "))
starting_number = int(input("Enter starting number: "))
ending_number = int(input("Enter ending number: "))

def generate_number(digits, start, end):
    number_chain = ""
    for i in range(digits):
        number_chain += str(random.randint(start, end)) + " "
        i = (i)
    return number_chain

print("Generated number chain:", generate_number(how_many_Digits, starting_number, ending_number))

