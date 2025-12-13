# 
#  Write a for loop with run in the range for (Moin, Ajija, Neamat, Arham) 
#  and print the house address under each name
# 
#  The address should be print by the "address(name)" function  
# 
#  Output : example 
# 
#   Moin
#   14 Howlett Crescent
#   Ajax, ON. L1T0A5
#
#   Ajija
#   14 Howlett Crescent
#   Ajax, ON. L1T0A5
#
#  And so on...
#


def address (name:str) :
    print(f"""
{name}
14 Howlett Crescent 
Ajax, ON. L1T0A5
          """)

names = ["Arham","Moin","Neamat","Ajija"] 

for name in names :
    address (name)

