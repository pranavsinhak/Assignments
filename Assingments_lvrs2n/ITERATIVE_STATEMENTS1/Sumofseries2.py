#Program to display the sum of the series 1,3,5,7,9,…,n
n = int(input("Enter the number:"))
sum_series = 0
print("Series:", end=' ')
for i in range(1, n+1):
    if i%2!=0:
        print(i, end=' ')
        sum_series += i
print(f"\nSum of the series: {sum_series}")