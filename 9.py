print("Voting Eligibility")
age = input("Enter age: ")

age=int(age)
if age >= 18 :
   print(f"Age:{age}\nYou are eligible to vote.")
else :
    print(f"Age:{age}\nYou are not eligible to vote")