print("Salary and Tax Calculator")
name = input("Name: ")
salary = int(input("Enter Salary: "))

salary=int(salary)
if 0 < salary < 100000 :
    net = salary
    print("No Tax")
elif 99999 < salary < 200000 :
    tax = salary * 0.05
    net = salary - tax
    print("5% Tax")
elif 199999 < salary < 400000 :
    tax = salary * 0.1
    net = salary - tax
    print("10% Tax")
else :
    tax = salary * 0.15
    net = salary - tax
    print("15% Tax")

print(f"Tax: {tax} \nNet Salary: {net}")