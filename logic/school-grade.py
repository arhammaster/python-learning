mathScore = int (input("What is your math score : "))
scienceScore = int (input("What is your science score : "))
languageScore = int (input("What is your language score : "))

totalScore = mathScore + scienceScore + languageScore

print ("your total score is : ", totalScore)

averageScore = totalScore / 3

print ("Your average score is : " , averageScore)

if averageScore <= 95 :
    print(" A+ ")
elif averageScore <= 90 and averageScore > 95 :
    print(" A ")
elif averageScore <= 85 and averageScore > 90 :
    print(" A- ")
elif averageScore <= 80 and averageScore > 85 :
    print(" B+ ")