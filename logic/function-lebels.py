# 
#  Write a for loop with run in the range for (max, Jill, Nancy, Abir) 
#  and print the house address under each name
# 
#  The address should be print by the "address(name)" function  
# 
#  Output : example 
# 
#   max
#   14 Green Crescent
#   Toronto, ON. L1T0A5
#
#   Jill
#   14 Green Crescent
#   Toronto, ON. L1T0A5
#
#  And so on...
#


def address (name:str) :
    print(f"""
{name}
14 Green Crescent 
Toronto, ON. L1T0A5
          """)

names = ["Abir","max","Nancy","Jill"] 

for name in names :
    address (name)

