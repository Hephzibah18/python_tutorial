# Extreme Spread
# Write a function calculate_range(numbers) that returns the 
# difference between minimum and maximum values.

def calculate_range(numbers):
    maximum = max(numbers)
    minimum = min(numbers)

    return maximum - minimum

result = calculate_range([4, 15, 2, 9])
print(f"Range: {result}")