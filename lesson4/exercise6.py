stack = []
stack.append("Bob")
stack.append("John")
print(stack)

temp = stack.pop(1)
print(temp + " served")

stack.append("Pat")

temp = stack.pop(1)
print(temp + " served")

print(stack)

