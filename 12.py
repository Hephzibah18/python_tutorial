print("Simple Shopping Calculator")
name = input("Product: ")
price = int(input("Price: "))
quantity = int(input("Quantity: "))
cost = price * quantity
print(f"Total: {cost}")

cost=int(cost)
if cost >= 5000 :
    print("You qualify for a discount.")
else :
    print("No discount available.")

