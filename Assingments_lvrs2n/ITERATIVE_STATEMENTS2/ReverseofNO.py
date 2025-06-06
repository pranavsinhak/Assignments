#Program to find the reverse of the given number
num = int(input("Enter the number:"))
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10

int(f"The reverse of the number: {reverse}")