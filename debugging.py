# Goal: Return total sum of positive numbers

def sum_positives(numbers):
    total = 0

    for i in range(len(numbers)): 
        if numbers[i] > 0: 
            total += numbers[i]
            
    return total 

result = sum_positives([3, -2, 5]) 
print("Result:", result)
