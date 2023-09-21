# Prompt the user to enter student's full name, ID number, course, and section
Studentsfullname = input("Student's full name: ")
IDnumber = input("ID number: ")
Course = input("Course: ")
Section = input("Section: ")

# Prompt the user to enter four quarter grades
Firstgrade = eval(input("1stgrade: "))
Secondgrade = eval(input("2ndgrade: "))
Thirdgrade = eval(input("3rdgrade: "))
Fourthgrade = eval(input("4thgrade: "))

# Compute the average of the four grades
average = (Firstgrade + Secondgrade + Thirdgrade + Fourthgrade) / 4

#Display results
print(Studentsfullname)
print(IDnumber)
print(Course)
print(Section)
print(Firstgrade)
print(Secondgrade)
print(Thirdgrade)
print(Fourthgrade)
print("The average of " + str(average))


