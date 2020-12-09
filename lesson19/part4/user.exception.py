class MyException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.value} is not valid"


try:
    val = int(input("Give an integer: "))
    if val < 0:
        raise MyException(val, "Invalid Value")
except MyException as e:
    print(e)
