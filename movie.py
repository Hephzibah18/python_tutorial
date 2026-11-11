def ticket_price(age):
    if 0 < age < 5:
        return 0
    elif 5 <= age <= 17:
        return 10
    else:
        return 20

age = int(input("Enter your age: "))

print(ticket_price(age))