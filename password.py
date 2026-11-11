correct_password = "python123"

password = input("Enter Password: ")

while password != correct_password:
     password = input("Enter Password: ")
else:
    print("Access Granted")