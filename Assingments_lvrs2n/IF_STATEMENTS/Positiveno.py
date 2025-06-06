#Program to determine quantum of profit or loss
cp = float(input("Enter the cost price of the item:"))
sp = float(input("Enter the selling price of the item:"))
if cp>sp:
    loss = cp - sp
    print(f"The seller has incurred a loss of Rs. {loss}.")
else:
    profit = sp - cp
    print(f"The seller has made a profit of Rs. {profit}.")