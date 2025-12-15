import random
moves = 0
number = (random.randint(1,100))

while moves < 10 :
    guess = int(input("Enter your guess :"))
    if guess > number :
        print("number is < then input")
        moves += 1
    elif guess < number :
        print("number is > then input")
        moves += 1
    elif moves == 10 :
        print("you ran out of guess")
    else :
        print(f"You guessed it right th number was {number} and it only took you {moves} guesses")
        break
