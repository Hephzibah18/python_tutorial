print("Exam Result")
name = input("Name: ")
maths = int(input("Mathematics Score: "))
english = int(input("English Score: "))
computer = int(input("Computer Score: "))
score = maths + english + computer 
average = score/3
print(f"Average: {average}")

average=float(average)
if average >= 50 :
    print("Result: Pass")
else :
    print("Result: Fail")    
