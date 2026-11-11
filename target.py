# 10. The Target Finder
# Goal: Write a function named find_element(items_list, target)
#  that loops through a list to find a specific target value. 
#  If the target is found, return its index position. If the 
#  loop finishes and the target is not in the list, return -1.
# Hint: Use for index in range(len(items_list)) to keep track 
# of the current position as you loop. Remember that a return 
# statement exits the function immediately when executed!


def find_element(items_list, target):
    for index in range(len(items_list)):
        if items_list[index] == target:
            return index

items = [1, 2, 3, 4, 5]
target = int(input("Enter a number: "))

result = find_element(items, target)

if result != -1:
    print(f"Index: {result}")
else:
    print("Index: -1")

