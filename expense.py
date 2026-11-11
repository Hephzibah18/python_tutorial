expenses = [2000, 1500, 3000, 2500, 1000]

total_expense = sum(expenses)

if total_expense > 8000:
    print("Overspending!")
else:
    print("Within Budget")

mimimum = min(expenses)
total = total_expense - mimimum

print(total)