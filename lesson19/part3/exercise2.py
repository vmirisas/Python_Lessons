class ValueTooSmallError(Exception):
    def __init__(self, message):
        self.message = message


class ValueTooLargeError(Exception):
    def __init__(self, message):
        self.message = message


class NotMultipleOfFiveError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} is not multiple of five"


def get_integer_con():
    while True:
        try:
            user_input = input("Give nonnegative integer: ")
            if user_input[0] == "-":
                st = user_input[1:]
                if st == "":
                    raise ValueError("No digits entered")
                elif not st.isdigit():
                    raise ValueError("Wrong input! Only digits please!")
                else:
                    raise ValueTooSmallError("value must be >= 100")
            else:
                st = user_input
                if st == "":
                    raise ValueError("No digits entered")
                elif not st.isdigit():
                    raise ValueError("Wrong input! Only digits please!")
                x = int(st)
                if x < 100:
                    raise ValueTooSmallError("value must be >= 100")
                elif x > 200:
                    raise ValueTooLargeError("value must be <= 200")
                elif x % 5 != 0:
                    raise NotMultipleOfFiveError(x)
        except(ValueTooSmallError, ValueTooLargeError, NotMultipleOfFiveError) as a:
            print(a)
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)
        else:
            print(x)
            break


print(get_integer_con())
