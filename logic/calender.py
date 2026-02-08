week_days = 7
max_weeks = 5
day = 1
days = 31
for i in range(max_weeks):
    if day == days+1 :
            break
    for j in range(1, week_days + 1 ):
        print(day, end=" ")
        day += 1
        if day == days+1 :
            break
    print()
    