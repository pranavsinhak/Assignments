# Program to find the factorial of a number
num = int(input("Enter the number:"))
if num < 0:
    print("Factorial is not defined.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i  
    print(f"Factorial of {num}: {factorial}")