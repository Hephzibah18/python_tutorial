print("Admission Checker")
name = input("Enter  Name: ")
age = int(input("Enter Age: "))
score = int(input("Enter Examination Score: "))

if age >= 16 and score >= 60 :
    print("Admission Approved")
elif age >= 16 and score < 60 :
    print("Admission Denied \nReason: Underperformed")
elif age < 16 and score >= 60 :
    print("Admission Denied \nReason: Underage")
else :
    print("Admission Denied \nReason: Underage and Underperformed")