#Program print the prime numbers between the 2 input numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"The prime numbers between {num1} and {num2}:")
for n in range(num1, num2+1):
    if n>1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=' ')