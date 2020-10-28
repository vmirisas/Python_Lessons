#immutable args dont keep the chamges out of the function
def f(arg):
    print(arg)
    arg = "Change!"
    print(arg)

s = "Initial"
print(s)
f(s)
print(s)