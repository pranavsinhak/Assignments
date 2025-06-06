#Program to determine whether a number is an Armstrong number or not
num = int(input("Enter a number:"))
order = len(str(num))
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp = temp//10
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")