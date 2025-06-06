#Write a program to accept two numbers from the user and swap their values. (Example: x=21, y=55; after swapping x=55, y=21)
x=int(input("Enter a value x:"))
y=int(input("Enter the value y:"))
x,y=y,x
print(f"After swaping:x = {x} and y = {y} ")
