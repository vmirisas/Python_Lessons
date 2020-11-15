from mod_pupils import *

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
            pupil_update(pupil)

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
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error, there is no pupil with that id")
                    continue
            elif delete_choice == 2:
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
            # Delete pupil
            delete_pupil_by_id(pupil["id"])
        elif choice == 5:
            print("Bye")
            break


main()
