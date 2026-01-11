word = str(input("What word do you want to check : "))
word = word.strip().lower()
word_len = len(word)

left = 0
right = word_len - 1

isPalindrome = True

while left < right :
    if word[left] == word[right] :
        left = left + 1
        right = right - 1
    else :
        isPalindrome = False
        break

if (isPalindrome) :
    print ("Palindrome")
else : 
    print ("Not palindrome")
