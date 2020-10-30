# globals
pupils = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "fathers_name": "Michael",
        "age": 15,
        "class": 1,
        "id_number": "AN123949"
    },
    {
        "id": 1002,
        "name": "Mary",
        "surname": "Poppins",
        "fathers_name": "Chris",
        "age": 10,
        "class": 3,
        "id_number": "AE123981"
    },
    {
        "id": 1003,
        "name": "John",
        "surname": "Wick",
        "fathers_name": "Chiwetel",
        "age": 7,
        "class": 6,

    },
    {
        "id": 1004,
        "name": "Bob",
        "surname": "Wick",
        "fathers_name": "Will",
        "age": 27,
        "class": 6,
        "id_number": "NA1234FS"
    }
]


# functions
def print_pupil(pupil):
    # print(f"id: {pupil['id']}")
    print(f"name:           {pupil['name']}")
    print(f"surname:        {pupil['surname']}")
    print(f"fathers name:   {pupil['fathers_name']}")
    print(f"age:            {pupil['age']}")
    print(f"class:          {pupil['class']}")
    if "id_number" in pupil:
        print(f"id number: {pupil['id_number']}")


def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)


def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['fathers_name'][0]}. {pupil['surname']}")


def next_id():
    ids = []
    for p in pupils:
        ids.append(p["id"])
    return max(ids) + 1


def create_pupil():
    name = input("Type name: ")
    surname = input("Type surname: ")
    fathers_name = input("Type father's name: ")

    for p in pupils:
        if p["name"] == name and p["surname"] == surname and p["fathers_name"] == fathers_name:
            print("this pupil already exists")
            ch = input("Do you want to continue? (y - yes, n - no)")
            if ch == "n":
                return None

    age = int(input("Type the age: "))
    pupil_class = int(input("Type the class: "))
    id_card = input("Does he/she has an id card: (y - true, n - false) ")
    if id_card == "y":
        id_number = input("Type the id card number: ")

    pupil = {}
    pupil["name"] = name
    pupil["surname"] = surname
    pupil["fathers_name"] = fathers_name
    pupil["age"] = age
    pupil["class"] = pupil_class
    if id_card == "y":
        pupil["id_number"] = id_number

    pupil["id"] = next_id()
    pupils.append(pupil)
    return pupil


def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            return pupil
    return None


def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil["surname"]:
            match_pupils.append(pupil)
    return match_pupils


def main():
    while True:
        print("\n==============")
        print("      MENU      ")
        print("1 - Create Pupil")
        print("2 - Print")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("5 - Exit")
        choice = int(input("Pick one: "))

        if choice == 1:
            print("NEW PUPIL")
            print("=========")
            pupil = create_pupil()
            if pupil is None:
                continue
            else:
                print("NEW PUPIL")
                print_pupil(pupil)

        elif choice == 2:
            print("\n==============")
            print("    SUB MENU     ")
            print("1 - Print Pupil")
            print("2 - Print All Pupils (details)")
            print("3 - Print All Pupils (names)")
            print_choice = input("Pick one: ")
            if print_choice.strip().isdigit():
                print_choice = int(print_choice)
            else:
                print("Wrong input")
                continue

            if print_choice == 1:
                pupil_id = int(input("Type the pupil's id: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil does not exist with this id")
                else:
                    print("     PUPIL      ")
                    print_pupil(pupil)
            elif print_choice == 2:
                print_pupils_details()
            elif print_choice == 3:
                print_pupils_names()
            else:
                print("Wrong input")
                continue
        elif choice == 3:
            print("\n==============")
            print("      SUB-MENU (UPDATE)      ")
            print("1 - Update Pupil (search by id)")
            print("2 - Update Pupil (search by surname)")
            update_choice = input("Pick one: ")
            if update_choice.strip().isdigit():
                update_choice = int(update_choice)
            else:
                print("Wrong input")
                continue
            if update_choice == 1:
                pupil_id = int(input("Type an id: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error, there is no pupil with that id")
                    continue
            elif update_choice == 2:
                pupil_surname = input("Type the students surname: ")
                matching_pupils = search_pupil_by_surname(pupil_surname)
                if matching_pupils == []:
                    print("No match found")
                    continue
                if len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(p)
                        print(f"id = {p['id']}")
                        print("=" * 15)
                    pupil_id = int(input("type an id: "))
                    pupil = search_pupil_by_id(pupil_id)

            # pupil update
            print_pupil(pupil)
            print("=" * 15)
            print("1 - name")
            print("2 - surname")
            print("3 - fathers_name")
            print("4 - age")
            print("5 - class")
            print("6 - id_number")
            update_choice = int(input("Pick a field to update: "))
            if update_choice == 1:
                pupil["name"] = input(f"Type a new name for student: ")
            elif update_choice == 2:
                pupil["surname"] = input(f"Type a new surname for student: ")
            elif update_choice == 3:
                pupil["fathers_name"] = input(f"Type a new fathers name for student: ")
            elif update_choice == 4:
                pupil["age"] = input(f"Type a new age for student: ")
            elif update_choice == 5:
                pupil["class"] = input(f"Type a new class for student: ")
            else:
                pupil["id_number"] = input(f"Type a new id number for student: ")

            print("=" * 15)
            print_pupil(pupil)
            print("Pupil updated")

        elif choice == 4:
            pass
        elif choice == 5:
            print("Bye")
            break


main()
