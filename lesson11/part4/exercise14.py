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

    }
]


# functions
def print_pupil(pupil):
    print(f"id: {pupil['id']}")
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
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Bye")
            break


main()
