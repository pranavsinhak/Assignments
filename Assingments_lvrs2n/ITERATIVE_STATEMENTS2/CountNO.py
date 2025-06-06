#Program to count the number of digits of a number
num = int(input("Enter a number:"))
count = 0
if num == 0:
    count = 1
else:
    while num!=0:
        num //= 10
        count += 1
print(f"The number of digits:{count}")