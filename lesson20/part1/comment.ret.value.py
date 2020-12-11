# "-> str" comments the returning type of a method
def full_name(first_name, last_name) -> str:
    return f"{first_name} {last_name}"


print(full_name("John", "Wick"))
