# 12 E Bill
try:
    units = float(input("Enter units consumed: "))
    if units < 0:
        raise ValueError("Units cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print(f"Units consumed: {units}")
finally:
    print(f"Total bill: Rs. {bill:.2f}")