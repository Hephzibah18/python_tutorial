print("ATM")

attempt = 3
pin = "5959"

atm = input("Enter Recipient Account Number: ")
amount = input("Enter Amount: ")

while attempt >= 1:
    pin_atm = input("ATM Pin: ")
    if pin_atm == pin:
        print("Transaction Successful ")
        print(f"Recipient: {atm}")
        print(f"Amount Debited: {amount}")
        break
    else:
        attempt -= 1
        print("Incorrect Pin")

    if attempt == 0:
        print("Card Blocked")
        print("Transaction Failed")
        break
        
