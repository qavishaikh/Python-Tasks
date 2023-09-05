number = int(input("Enter Table Number: "))
range_Lmit = 10

print(f"Multiplication Table of {number}")
for i in range(1, range_Lmit + 1):
    if number > 5:
        print("Enter Number 1 to 5")
        break
    else:
        result = number * i
        print(f"{number} x {i} = {result}")
print("Crated By Qavi Shaikh!")