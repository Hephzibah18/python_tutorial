# 8. The Odd Counter
# Goal: Write a function named count_odds(numbers_list) that takes a list 
# of integers and returns 
# the total count of how many odd numbers are in that list.
# Hint: Set up a counter variable at 0. Loop through the list, and use 
# an if statement with % 2 != 0 
# to check if a number is odd. If it is, increment your counter.

def count_odds(numbers_list):
    count = 0
    for number in numbers_list:
        if number % 2 != 0:
            count += 1
    return count

numbers = [1, 2, 3, 4, 5]

result = count_odds(numbers)
print(result) 