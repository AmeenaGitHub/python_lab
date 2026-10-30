# 3 Fibonacci series upto n

l = int(input("Enter a limit: "))
print("Fibonacci series upto",l,":")
a,b = 0,1
for i in range(l):
    print(a)
    a,b = b, a+b