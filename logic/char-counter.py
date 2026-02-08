# Take input string
# Take character to be count into string

# Input > I Love Python Programming
# Inout > Character lookup : o
# 
# Output > o : 3 

word = str(input("Input Paragraph : "))
character_look_up = str(input("Character to look up : "))
word_character = len(word)
character_count = 0

for i in range (0,word_character ) :
    if character_look_up in word[i] :
        character_count += 1

print (f"Character count {character_count}")