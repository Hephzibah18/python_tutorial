# 6. Blastoff Countdowns
# Goal: Write a function named countdown(start) that takes a starting number and 
# uses a while loop to print a countdown down to 1, followed by printing "Blastoff!".
# Hint: Inside the while loop, make sure you decrease your starting number by 1 
# each time so the loop doesn't run forever.

# Phase 3: Combining Functions, Loops, and Conditions
# These challenges require combining all three concepts to solve more realistic problems.

def countdown(start):
    while start >= 1:
        print(start)
        start = start - 1
    print("Blastoff!")

countdown(5)

