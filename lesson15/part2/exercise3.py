def copy_file(filename1, filename2):
    with open(filename2, "r") as f:
        contents = f.read()

    with open(filename1, "w") as f:
        f.write(contents)


copy_file("test3.txt", "..\\part1\\test2.txt")
