print("Largest of two Numbers")
first = input("Enter first number: ")
second = input("Enter second number: ")

first=float(first)
second=float(second)
if first == second :
    print(f"The two numbers are equal.")
else :    
   if first > second :
    print(f"The larger number is {first}")
   else :
    print(f"The larger number is {second}")    