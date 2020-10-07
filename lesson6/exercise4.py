prime_list= []
for n in range(2,100+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        prime_list.append(n)
prime_tuple = tuple(prime_list)
print(prime_tuple)