#Program to find sum of digits until sum gets to be a single digit number.
num = int(input("Enter the number:"))
while num>=10:
    sum_of_digits = 0
    while num>0:
        sum_of_digits += num%10
        num = num//10
    num = sum_of_digits
print(f"The single digit sum: {sum_of_digits}")