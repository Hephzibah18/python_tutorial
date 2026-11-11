print("Simple Login")

correct_username = "Hephzibah"
correct_password = "11111"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username and password == correct_password:
    print(f"Login Successful.\nWelcome back, {username}!")
else :
    print(f"Login Failed.\nIncorrect Username or Password.")     