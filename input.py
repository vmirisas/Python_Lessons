name = input("type your name: ")
surname = input("type your surname: ")
age = int(input("type your age: "))
magic_pill = 10
age -= magic_pill
message_name = "Hello " + name + " " + surname
message_age = ". You are " + str(age) + " years old!"
message = message_name + message_age
print(message)

