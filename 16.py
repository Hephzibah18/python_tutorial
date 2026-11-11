print("Student Performance Report")
name = input("Name: ")
maths = int(input("Mathematics Score: "))
english = int(input("English Score: "))
physics = int(input("Physics Score: "))

total = maths + english + physics
average = total/3
print(f"Total Score: {total}\n Average Score: {average}")

average=int(average)
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