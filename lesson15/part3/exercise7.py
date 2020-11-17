def merge(filename1, filename2, filename3):
    with open(filename3, "a") as file3:
        with open(filename1) as file1:
            contents = file1.read()
        file3.write(contents)

        with open(filename2) as file2:
            contents = file2.read()
        file3.write(contents)

merge("..\\part1\\test.txt", "..\\part1\\test2.txt", "test4.txt")