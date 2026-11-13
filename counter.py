# Threshold Counter
# Write a function count_above(numbers, limit) that
# counts items strictly greater than limit.

def count_above(numbers, limit):
    count = 0

    for i in range(len(numbers)): 
        if numbers[i] > limit: 
            count += 1
            
    return count

result = count_above([10, 25, 8, 30], 20)
print(f"Result: {result}")