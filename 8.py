print("Grade Classifier")
score = input("Enter score: ")

score=int(score)
if 70 <= score <= 100 :
   print(f"Score: {score} \nGrade: A")
elif 70 > score > 59 :
   print(f"Score: {score}\nGrade: B")
elif 49 < score < 60 :
   print(f"Score: {score}\nGrade: C")
elif 39 < score < 50 :
   print(f"Score: {score}\nGrade: D")   
else :
   print(f"Score: {score}\nGrade: F")