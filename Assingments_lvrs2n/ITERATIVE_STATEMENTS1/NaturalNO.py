#calculate the sum of natural number series
num = int(input("Enter a number:"))
print("Natural number series:", end=' ')
for i in range(1, num+1):
    print(i, end=' ')
total = sum(range(1, num+1))
print(f"\nSum of the series= {total}")