from teachers import Teachers
from pupils import Pupils


def main():
    pupils = Pupils()
    teachers = Teachers()

    while True:
        print("\n==============")
        print("      MENU      ")
        print("1 - Create Pupil")
        print("2 - Print")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("5 - Create Teacher")
        print("6 - Read Teacher")
        print("7 - Update Teacher")
        print("8 - Delete Teacher")
        print("9 - Exit")
        choice = int(input("Pick one: "))

        if choice == 1:
            print("NEW PUPIL")
            print("=========")
            pupil = pupils.create_pupil()
            if pupil is None:
                continue
            else:
                print("NEW PUPIL")
                print(pupil)

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
                pupil = pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil does not exist with this id")
                else:
                    print("     PUPIL      ")
                    print(pupil)
            elif print_choice == 2:
                print(pupils)
            elif print_choice == 3:
                pupils.print_pupils_names()
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
                pupil = pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error, there is no pupil with that id")
                    continue
            elif update_choice == 2:
                pupil_surname = input("Type the students surname: ")
                matching_pupils = pupils.search_pupil_by_surname(pupil_surname)
                if not matching_pupils:
                    print("No match found")
                    continue
                if len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print(p)
                        print(f"id = {p['id']}")
                        print("=" * 15)
                    pupil_id = int(input("type an id: "))
                    pupil = pupils.search_pupil_by_id(pupil_id)

            # pupil update

            pupils.pupil_update(pupil)

        elif choice == 4:
            print("\n==============")
            print("      SUB-MENU (DELETE)      ")
            print("1 - Delete Pupil (search by id)")
            print("2 - Delete Pupil (search by surname)")
            delete_choice = input("Pick one: ")
            if delete_choice.strip().isdigit():
                delete_choice = int(delete_choice)
            else:
                print("Wrong input")
                continue

            if delete_choice == 1:
                pupil_id = int(input("Type an id: "))
                pupil = pupils.search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error, there is no pupil with that id")
                    continue
            elif delete_choice == 2:
                pupil_surname = input("Type the students surname: ")
                matching_pupils = pupils.search_pupil_by_surname(pupil_surname)
                if not matching_pupils:
                    print("No match found")
                    continue
                if len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print(p)
                        print(f"id = {p['id']}")
                        print("=" * 15)
                    pupil_id = int(input("type an id: "))
                    pupil = pupils.search_pupil_by_id(pupil_id)
            # Delete pupil
            pupils.delete_pupil_by_id(pupil.pupil_id)
        elif choice == 5:
            first_name = input("Type teachers name: ")
            surname = input("Type teachers surname: ")
            teachers.create_teacher(first_name, surname)
        elif choice == 6:
            teacher_id = int(input("type the teacher's id: "))
            teacher = teachers.read_teacher(teacher_id)
            if teacher is None:
                print("No such teacher exists")
            else:
                teacher.print_teacher()
        elif choice == 7:
            teacher_id = int(input("type the teacher's id: "))
            teachers.update_teacher(teacher_id)
        elif choice == 8:
            teacher_id = int(input("type the teacher's id: "))
            teachers.delete_teacher(teacher_id)
        elif choice == 9:
            print("Bye")
            teachers.save_teachers_data()
            pupils.save_pupils_data()
            break


main()
