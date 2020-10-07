semester_grades = [4, 6, 3, 8, 10]
passed = 0
sum_grades = 0
for grade in semester_grades:
    if grade >= 5:
        passed += 1
        sum_grades += grade
print("number of passed lessons: " + str(passed))
print("average grade of the semester: " + str(sum_grades / passed))
