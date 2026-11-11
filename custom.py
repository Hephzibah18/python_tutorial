# 4. The Custom Multiplier Table
# Goal: Write a function named multiplication_table(number, limit) that prints the
# multiplication table for a given number up to the specified limit.
#   For example, multiplication_table(5, 3) should print:
# text
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# Use code with caution.
# Hint: Use a for loop combined with the range() function inside your block.
# This function does not need a return statement; it just needs to print.

def multiplication_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} * {i} = {number * i}")

answer = multiplication_table(5, 3)


