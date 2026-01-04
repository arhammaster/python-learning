# print triangle as 
#
# Input : Python
#
# Output
#
# P
# YY
# TTT
# HHHH
# OOOOO
# NNNNNN 

word = str(input("What word do you want to rewriting triangle writing : "))

word = word.strip()

length = len(word)

print("--------------------------------------")
for i in range (length) :
    for j in range (i+1) :
        print(word[i].upper(), end="")
    print()
print("--------------------------------------")
#
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
#
print("--------------------------------------")
for i in range (length) :
    for j in range (i+1) :
        print(word[j].upper(), end="")
    print()
print("--------------------------------------")
#
#      P
#     PY
#    PYT
#   PYTH
#  PYTHO
# PYTHON
#

print("--------------------------------------")
# i loop for line
for i in range (length) :
    # j loop for space 
    for j in range (length - i) :
        print(" ", end="")
    # k loop for character
    for k in range (i+1) :
        print(word[k].upper(), end="")
    print()
print("--------------------------------------")
