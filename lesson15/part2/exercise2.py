with open("..\\part1\\test2.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][len(lines[i])-1] == "\n":
        lines[i] = lines[i][:len(lines[i])-1]

print(lines)
print(len(lines[0]))