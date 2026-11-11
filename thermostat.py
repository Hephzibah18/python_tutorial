print("Smart Thermostat")
current_temp = 20

temp = int(input("Enter Temperature: "))
while current_temp != temp :
    if current_temp < temp :
        current_temp += 1
    else :
        current_temp -= 1

print(f"Current Temperature: {current_temp}")        

