#Program to find m^n
m = int(input("Enter the value of m:"))
n = int(input("Enter the value of n:"))
result = 1
i = 1
while i<=n:
    result *= m
    i += 1
print(f"The value of {m}^{n}:{result}")