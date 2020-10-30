def print_full_name(first_name, surname, details=False):
    if details:
        print("First Name: " + first_name)
        print("Surname: " + surname)
    else:
        print(f"{first_name} {surname}")


print_full_name("Charles", "Kane")
print_full_name("Charles", "Kane", True)
