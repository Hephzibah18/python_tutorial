print("Shopping Receipt")
name = input("Name: ")
product1 = input("First Product: ")
price1 = float(input(f"Price of {product1}: ")) 
product2 = input("Second Product: ")
price2 = float(input(f"Price of {product2}: ")) 
product3 = input("Third Product: ")
price3 = float(input(f"Price of {product3}: "))

discount = 0
sub_total = price1 + price2 + price3

if sub_total >= 10000 :
    discount = sub_total * 0.1
    total = sub_total - discount
elif sub_total >= 5000 and sub_total <= 10000 :
    discount = sub_total * o.o5
    total = sub_total - discount

else :
    total = sub_total
    print(f"{name}'s Receipt \n{product1}: {price1} \n{product2}: {price2} \n{product3}: {price3} ")


print(f"Subtotal: {sub_total} \nDiscount: {discount} \nFinal Total: {total}")