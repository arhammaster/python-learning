# find the next date from the given date 
# 
# Example 
# 
#  Input 
#
#   Enter Day : 5
#   Enter Month : 2
#   
#  Output
#  
#   Today is 5 / 2
#   Yesterday will 4 / 2

day:int = int (input("Enter Day : "))
month:int = int(input("Enter Month : "))
year:int  = int (input("Enter Year : "))

previousDay:int = day
previousMonth:int = month
previousYear:int = year

print("Today is ", day, "/", month, "/", year)

if month == 1 and day == 1:
    previousDay = 30
    previousMonth = 12
    previousYear = year - 1
elif day ==  1:
    previousDay = 30
    previousMonth = month - 1
else :
    previousDay = day- 1   

    

print("Yesterday is ", previousDay, "/",previousMonth, "/", previousYear)

