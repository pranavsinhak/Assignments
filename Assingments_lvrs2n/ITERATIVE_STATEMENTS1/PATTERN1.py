#program to print the number pattern
num = 1
rows =[1, 2, 4, 4]
for count in rows:
    for i in range(count):
        print(num, end=' ')
        num+=1
    print()