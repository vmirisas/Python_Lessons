def input_float():
    while True:
        float_input = input("Type a number: ").strip()
        if "." in float_input:
            parts = float_input.split(".")
            if len(parts)>2:
                print("type only one dot")
            elif parts[0].isdigit() and parts[1].isdigit():
                return float(float_input)
            else:
                print("wrong input, type a float number!")
        else:
            if float_input.isdigit():
                return float(float_input)
            else:
                print("Type digits only! ")



given_number = input_float()
print(given_number)
print(type(given_number))