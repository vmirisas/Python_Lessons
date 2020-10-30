def print_full_name(first_name, surname, second_name="", second_surname="", details=False):
    if details:
        if second_name != "":
            print("First Name: " + first_name + "-" + second_name)
        else:
            print("First Name: " + first_name)
        if second_surname != "":
            print("Surname: " + surname + " " + second_surname)
        else:
            print("Surname: " + surname)
    else:
        if second_name != "":
            print(f"{first_name}-{second_name} {surname} {second_surname}")
        else:
            print(f"{first_name} {surname} {second_surname}")

print_full_name("Charles", "Kane", "Bob")
print_full_name("Charles", "Kane", second_surname="Foster")
print_full_name("Charles", "Kane", "Bob", second_surname="Foster")
print_full_name("Charles", "Kane", details=True)
