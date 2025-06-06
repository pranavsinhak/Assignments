#Program to find the factorial of the number
num = int(input("Enter the number:"))
factorial = 1
i = 1
while i<=num:
    factorial *= i
    i += 1
print(f"The factorial of {num} is {factorial}.")