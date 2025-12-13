# online shopping store give discount on total bill amount by bellow algorithm 

# bill amount is more then 1000 then 100 off 
# bill amount is more then 500 and less then 1000 then 50$ off
# bill amount id more then 250 and less then 500 then 20$ off
# bill amount is more then 150 and less then 250 then 10$ off 
# bill amount is less then 150 then there is not discount 
# 
# As a developer write a code to calculate bill amount after discount
# 
# Input 
# Enter Bill Total : 1000
# 
# Output
# After Discount Bill Total : 900
# 

billAmount:int = int(input("Enter Total Bill : ")) 

discount:int = 0

if billAmount >= 1000 :
    discount = 100
elif  billAmount >= 500 and billAmount < 1000 :
    discount = 50
elif  billAmount >= 250 and billAmount < 500 :
    discount = 20
elif  billAmount >= 150 and billAmount < 250 :
    discount = 10
else :
    discount = 0

billAfterDiscount:int = billAmount - discount        

print("After Discount bill is :", billAfterDiscount)