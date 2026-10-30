# 1.1 Area of circle 

print("Area of circle")
r = int(input("Radius of circle: "))
a = 3.14*r*r
print("Area of circle = ", a)

# 1.2 Check leap year

print("Check leap year")
yr = int(input("Enter a year: "))
if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print(yr, "is a Leap year")
else:
    print(yr, "is not a leap year")

# 1.3 Largest of 3 num

print("Largest of 3 numbers")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a >= b and a >= c:
    print(a, "is greatest.")
elif b >= a and b >= c:
    print(b, "is greatest.")
else:
    print(c, "is greatest.")