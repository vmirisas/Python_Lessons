def function(*grades, **surname_lesson):
    print(surname_lesson)
    sum = 0
    for grade in grades:
        sum += grade
    average = sum / len(grades)
    print(average)

    dictionary = {}
    for key, value in surname_lesson.items():
        if value in dictionary:
            dictionary[value] += [key]
        else:
            dictionary[value] = [key]
    print(dictionary)
function(5, 1, 5, 7, 9, 10, 4, 6, Banner="Discrete Mathematics", Stark="Programming", Kane="Discrete Mathematics")
