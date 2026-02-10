#  Ask user to enter name and print each letter into new line 
#  
#  Input : 
#  
#       Enter your name : Arjun
#  
#  Output :
#  
#       A
#       r
#       h
#       a
#       m

word = (input("What word : "))

word_length = len(word)

for i in range (word_length) :
    print( "\t" + word[i])