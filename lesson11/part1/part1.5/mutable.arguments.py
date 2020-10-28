#mutable args keep their changes out of the function, since they are not registrations
def f(arg):
    print(arg)
    arg.append(3)
    print(arg)

l = [1,2]
print(l)
f(l)
print(l)