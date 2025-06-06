#Program to display the sum of the series 1/2^3+1/3^3+1/4^3+……….+1/n^3
n = int(input("Enter the number:"))
total = 0
for i in range(2, n+1):
    total += 1/(i**3)
    print(f"\nSum of the series: {total}")