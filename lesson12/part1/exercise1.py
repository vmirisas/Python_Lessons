def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    return fact
print(factorial(5))
