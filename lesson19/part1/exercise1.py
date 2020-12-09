filename = "filename.txt"
try:
    with open(filename) as f:
        st = f.read()
except FileNotFoundError:
    print(f"the file '{filename}' does not exist")
    choice = input("Do you want to create the file? (Y/N): ")
    if choice == "y" or choice == "Y":
        with open(filename, "w") as f:
            pass