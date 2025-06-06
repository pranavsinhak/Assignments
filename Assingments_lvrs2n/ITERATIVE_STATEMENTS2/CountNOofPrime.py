#Program to find the count of the digits that are prime numbers.
num = int(input("Enter the number:"))
count = 0
while num>0:
    digit = num%10
    if digit in [2,3,5,7]:
        count += 1
    num = num//10
print(f"Number of prime digits: {count}")
