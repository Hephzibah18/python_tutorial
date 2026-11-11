names = ["Winifred", "Hephzibah", "Delight", "Gloria", "Queen"]

name = input("Enter a Name: ")

if name in names:
        print(f"{name} Found")
else:
        print(f"{name} Not Found")