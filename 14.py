print("Simple ATM Decision")
balance = float(input("Account Balance: "))
amount = float(input("Withdrawal Amount: "))
remain = balance - amount

if balance < amount :
    print("Transaction Declined.\n Reason: Insufficient Balance.")
else :
    print("Withdrawal Successful.")
    print(f"Amount Withdrawn: ₦{amount}")
    print(f"Remaining Balance: ₦{remain}")