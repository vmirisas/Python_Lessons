age = int(input("type your age : "))
if age < 18:
    print("you are underage")
elif 18 <= age < 65:
    print("you are an adult")
else:
    print("you are retired")