semester_grades = [2, 3, 5, 7, 9]
passed = 0
sum_grades = 0
for grade in semester_grades:
    if grade >= 5:
        passed += 1
        sum_grades += grade

print("i've passed in: " + str(passed) + " lessons")

print("average grade is " + str(sum_grades / passed))
