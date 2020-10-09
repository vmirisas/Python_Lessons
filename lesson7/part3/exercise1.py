N = 5
A = {number for number in range(1,6)}
print(A)

result = set()
for i in A:
    
    result.add((i , i**2))
print(result)