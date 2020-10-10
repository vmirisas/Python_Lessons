N = 100
even_set = set()
odd_set = set()
multiples_3 = set()
primes_set = set()

for number in range(0, N+1):
    if number % 2 == 0:
        even_set.add(number)
    else:
        odd_set.add(number)

print(even_set)
print(odd_set)


for number in range(0, N+1):
    if number % 3 == 0:
        multiples_3.add(number)
print(multiples_3)

for number in range(2, N+1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes_set.add(number)
print(primes_set)

set1 = even_set | multiples_3
print(set1)

set2 = odd_set & primes_set
print(set2)

set3 = primes_set - odd_set
print(set3)

set4 = primes_set ^ odd_set
print(set4)