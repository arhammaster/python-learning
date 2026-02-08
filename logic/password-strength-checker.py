# password strength check based on the character counts
# 
# Score Password as
# if 


password = input("Enter the password : ")
password_length = len(password)

if password_length > 8 and password_length < 16 :
    print("Valid password")

    

else :
    print("Invalid password, It must have 8 to 16 characters")