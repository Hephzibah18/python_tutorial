# 5. The Accumulator
# Goal: Write a function named sum_up_to(n) that takes an integer n and returns the
#  sum of all numbers from 1 up to n. For example, sum_up_to(4) should return 10 
#  (because 1 + 2 + 3 + 4 = 10).
# Hint: Initialize a tracking variable (like total = 0) before your loop, and add
#  the loop variable to it on every iteration.


def sum_up_to(n):
    all_num = range(1, n+1)
    total = 0
    for num in all_num:
        total += num
    print(total)

sum_up_to(4)



