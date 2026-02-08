

print("Jan , Feb , Mar , Apr , May , Jun , Jul , Aug , Sep , Oct , Nov , Dec")

what_month = "a"

what_month = str(input("What month : "))

what_month = what_month.strip().title()

if what_month == "Jan" or what_month == "March" or what_month == "May" or what_month == "Jul" or what_month == "Oct" or what_month == "Dec" :
    month = 7
    weeks = 5
    days = 1
    for i in range(weeks):
        for j in range(1, month + 1 ):
            print(days, end=" ")
            days = days + 1
            if days == 32 :
                break
        print()
elif what_month == "Feb" :
    month = 7
    weeks = 5
    days = 1
    for i in range(weeks):
        for j in range(1, month + 1 ):
            print(days, end=" ")
            days = days + 1
            if days == 29 :
              break
        print()
elif what_month == "Apr" or what_month == "Jun" or what_month == "Aug" or what_month == "Sep" or what_month == "Nov" :
    month = 7
    weeks = 5
    days = 1
    for i in range(weeks):
        for j in range(1, month + 1 ):
            print(days, end=" ")
            days = days + 1
            if days == 31 :
                break
        print()