def digits_print(number):
    digits = [int(d) for d in str(number)]
    if len(digits) != 3:
        print("number must have 3 digits")
    else:
        print(f"1st digit: {digits[0]}")
        print(f"2nd digit: {digits[1]}")
        print(f"3rd digit: {digits[2]}")


def digits(number):
    digits = [int(d) for d in str(number)]
    if len(digits) != 3:
        return
    else:
        return digits[0], digits[1], digits[2]


digits_print(234)

a, b, c = digits(987)
print(a)
print(b)
print(c)

print(digits(345623456))
