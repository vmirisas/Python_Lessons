teachers = [
    {
        "id": 1001,
        "name": "Severus",
        "surname": "Snape",
    },
    {
        "id": 1002,
        "name": "Charles",
        "surname": "Xavier",

    },
    {
        "id": 1003,
        "name": "Sergio",
        "surname": "Marquina",
    }
]


def next_id():
    ids = []
    for t in teachers:
        ids.append(t["id"])
    return max(ids) + 1


def create_teacher(first_name, surname):
    for teacher in teachers:
        if teacher["name"] == first_name and teacher["surname"] == surname:
            print("Error, this teacher already exists")
            return None
    t = {"id": next_id(), "name": first_name, "surname": surname}

    teachers.append(t)
    return teachers


def read_teacher(teacher_id):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            return teacher
        else:
            return None


def update_teacher(teacher_id, key, value):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            teacher[key] = value
            return


def delete_teacher(teacher_id):
    for i in range(len(teachers)):
        if teacher_id == teachers[i]["id"]:
            teachers.pop(i)
            return


def print_teacher(teacher):
    print(f"Name:    {teacher['name']}")
    print(f"Surname: {teacher['surname']}")
    print(f"id:      {teacher['id']}")

def print_all_teachers():
    for teacher in teachers:
        print("="*20)
        print_teacher(teacher)
