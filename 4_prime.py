# 4 Prime or not

n = int(input("Enter a number: "))
if n <= 0:
    print("Enter a positive integer greater than 0.")
else:
    c = 0
    for i in range(1, n+1):
        if (n % i == 0):
            c += 1    
    if c == 1:
        print("1 is neither prime nor composite ;)")
    elif c == 2:
        print(n, "is a prime number.")
    else:
        print(n, "is a composite number.")