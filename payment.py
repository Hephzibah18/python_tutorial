print("Payment")
target = 20000
total = 0

while total < 20000:
    payment = int(input("Enter payment: "))
    total += payment

    print(f"Total payment received: {total}")

print("Target amount reached!")