n = 7
if n == 0 or n==1:
    print("not a prime number")
else:
    for i in range(2,n):
        if n % i ==0:
            print("not a prime number")
            break
    else:
        print("its a prime number")