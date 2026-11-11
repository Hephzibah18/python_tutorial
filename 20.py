print("Mini Student Report System")
name = input("Enter Name: ")
age = input("Enter Age: ")
maths = float(input("Enter Mathematics Score: "))
english = float(input("Enter English Score: "))
python = float(input("Enter Python Score: "))
total = maths + english + python
average = total/3
average=round(average,2)
print(f"Total Score: {total} \nAverage Score: {average}")

if 69 < average < 101 :
    print("Grade: A")
elif 59 < average < 70 :
    print("Grade: B")
elif 49 < average < 60 :
    print("Grade: C")
elif 39 < average < 50 :
    print("Grade: D") 
else :
    print("Grade: F")

if average >= 80 :
    print("Excellent Performance!")
elif 59 < average < 80 :
    print("Good Performance")
else :
    print("Keep Practicing")