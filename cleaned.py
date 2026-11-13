# Cleaned List Sum
# Write a function sum_without_outlier(scores) that 
# removes the lowest and the highest value from a list,
# then returns the sum of the remaining numbers.

def sum_without_outlier(scores):
    scores.remove(max(scores))
    scores.remove(min(scores))
    sum = 0

    for i in range(len(scores)): 
        if scores[i] != min and scores[i] != max: 
            sum += scores[i]
            
    return sum

result = sum_without_outlier([10, 2, 8, 4, 20])
print(f"Result: {result}")


