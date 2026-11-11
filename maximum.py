# 3. Maximum of Three
# Goal: Write a function named find_max(a, b, c) that takes three numbers as arguments 
# and returns the largest of the three. (Do not use Python's built-in max() function!)
# Hint: Use conditional statements to compare the variables against one another.


def find_max(a, b, c):
    if a > b and a > c:
        print(f"Largest number - {a}")
    elif b > a and b > c:
        print(f"Largest number - {b}")
    else:
        print(f"Largest number - {c}")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

find_max(a, b,)
    