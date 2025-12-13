# find the next date from the given date 
# 
# Example 
# 
#  Input 
#
#   Enter Day : 1
#   Enter Month : 2
#   Enter Year : 2025
#   
#  Output
#  
#   Today is 1/2/2025
#   Tomorrow will 2/2/2025

day:int = int (input("Enter Day : "))
month:int = int (input("Enter Month : "))
year:int = int (input("Enter Year : "))

print("Today is ", day, "/", month, "/", year)

# every month is end pon 30th, there is no 31 and 28 handling for now
endOfTheDay:int = 30

# next day initialization 
tomorrowDay:int = day
tomorrowMonth:int = month
tomorrowYear:int = year

# next day calculation

if(day+1 > 30) :
    if(month+1 > 12) :
        tomorrowYear = year+1
        tomorrowMonth=1
        tomorrowDay=1
    else :
        tomorrowMonth = month+1 
        tomorrowDay = 1
else :
    tomorrowDay = day+1

print("Tomorrow will ", tomorrowDay, "/", tomorrowMonth, "/", tomorrowYear)
