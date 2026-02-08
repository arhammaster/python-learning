# Define dictionary with student role number 
#
# 1 : John
# 2 : Smith
# 3 : Mario
#
# Print the name based on role number which user give into input 
#
#
# Input > "Enter Student Role Number : "  1
# Output : John 
#
# If the Input is 4 then Output should be "Student Does Not Exist"

students = {
    "1" : "John",
    "2" : "Smith",
    "3" : "Mario",
    "4" : "Tom"
}

role_number = input("Enter Student Role Number : ")

if role_number not in students :
    print("Student Does Not Exist")
else :
    print(students[role_number])

new_student = {"5" : "Jerry"}
students.update(new_student)
print(students)
print(students["5"])

del students["2"]
print(students)





