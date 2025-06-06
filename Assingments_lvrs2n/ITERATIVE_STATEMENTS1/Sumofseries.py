#Program to display the sum of the series 1+1/2+1/3+……….+1/n
n = int(input("Enter the number:"))
total = 0
for i in range(1, n+1):
    total += 1/i
    print(f"\nSum of the series: {total}")