string = "Sample String"

print("print three times the variable 'string': " + (string + " ") * 3)
print("print the [indexed] char of the 'string': " + string[1])
print("print slices of of the 'string': " + string[1:4] + string[-4:-1])
print("print the length of the 'string':" + str(len(string)))
print("print the max alphabetically character: " + str(max("sample")))
print("print the min alphabetically character: " + str(min("String")))
print("print the index of the sub-string in the string : " + str(string.index("am")))
print("print the number of the existing char in the string: " + str(string.count("S")))
# if str[2] = "c" not working...change the indexed character of the string
new_str = string[:2] + "c" + string[3:]
print(new_str)
