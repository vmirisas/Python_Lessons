from random import randrange


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1

    def __lt__(self, other):
        return self.grade < other.grade

    def __str__(self):
        return f"{self.full_name}: {self.grade}"


def grade_student(student):
    student.grade = randrange(0, 11)


def average(students):
    s = 0
    for student in students:
        s += student.grade

    print(f"The average grade of the students is: {s / len(students)}")


names = ["Stefanie Prentice",
         "Mohamad Allan",
         "Zainab Dickson",
         "Douglas Oneil",
         "Ana Nash",
         "Leonidas Keenan",
         "Isaac Ashley",
         "Angelina Tang",
         "Natasha Miranda",
         "Christopher Paterson"]

students = [Student(names[i]) for i in range(len(names))]

for student in students:
    grade_student(student)
    print(f"{student.full_name}: {student.grade}")
print("")

average(students)
print("")

students.sort(reverse=True)
for student in students:
    print(student)
