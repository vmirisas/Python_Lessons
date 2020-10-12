string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed libero vitae est rhoncus cursus at eget eros. Phasellus laoreet lobortis suscipit. Duis pretium felis quis tristique lacinia. Nulla id convallis dolor, ac dapibus lectus. Maecenas gravida ut arcu sit amet ultrices. Quisque ut massa sit amet nibh placerat tempor. Vivamus lacus felis, iaculis et nunc id, condimentum dapibus ligula."

print(string)

str_list = list(string)
print(type(str_list))
print(str_list)

dictionary = {}
for char in str_list:
    if char not in dictionary:
        dictionary[char] = 0
    else:
        dictionary[char] += 1
print(dictionary)

max_num = 0
for values in dictionary:
    if dictionary[values] >= max_num:
        max_num = dictionary[values]
print(max_num)

print(max(list(dictionary.values())))

for key, value in dictionary.items():
    if value == max_num:
        if key == " ":
            print("blank")
        else:
            print(key)
