print("Temperature Checker")
temp = input("Enter Temperature: ")
temp_int=int(temp)
if temp_int >= 30 :
   print("It is hot")
elif 20 < temp_int < 30 :
    print("The weather is warm")
else :
    print("It is cold")      