print("ATM Pin Validator")
attempt = 3
pin = "5959"
while attempt >= 1:
    pin_atm = input("ATM Pin: ")
    if pin_atm == pin:
        print("Access Granted")
        break
    else:
        attempt -= 1
        print("Incorrect Pin")

    if attempt == 0:
        print("Card Blocked")
