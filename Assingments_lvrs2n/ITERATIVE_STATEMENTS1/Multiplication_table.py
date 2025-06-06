#Program to print multiplication table upto 10 times.
num = int(input("Enter the number:"))
print(f"Multiplication table of {num}:\n")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")