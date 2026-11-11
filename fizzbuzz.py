# 7. The FizzBuzz Function
# Goal: Write a function named fizzbuzz_up_to(limit) that loops from 1
# up to the limit. For each number, it should print:
# "Fizz" if the number is divisible by 3.
# "Buzz" if the number is divisible by 5.
# "FizzBuzz" if it is divisible by both 3 and 5.
# The number itself if it is divisible by neither.
# Hint: Use the modulo operator % to check for divisibility (e.g., num % 3 == 0). 
# Check for the combined "FizzBuzz" condition first!

def fizzbuzz_up_to(limit):
    for num in range(1, limit):
        if num %  3 == 0:
            print(f"Fizz! {num} is divisible by 3")
        elif num %  5 == 0:
            print(f"Fizz! {num} is divisible by 5")
        elif (num %  3 == 0) and (num %  5 == 0):
            print(f"FizzBuzz! {num} is divisible by 3 and 5")
        elif not (num %  3 == 0) and (num %  5 == 0):
            print(num)
fizzbuzz_up_to(20)
    
