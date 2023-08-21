'''
Write a function MaxvalueSelection(items, C) that accepts a dictionary items where each key
of the dictionary represents the item name and the corresponding value is a tuple (number of
units, value of all units) and function accept one more variable c which represents the
maximum capacity of units you can select from all items to get maximum value.

Sample input
{1:(10,60),2:(20,100),3:(30,120)}

Output
240
'''

def MaxvalueSelection(items, C):
    # Convert the items dictionary into a list of tuples with weight and value per unit
    items_list = [(weight, value / weight) for weight, value in items.values()]

    # Sort the items by value per unit in descending order
    items_list.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the total value and remaining capacity
    total_value = 0
    remaining_capacity = C

    # Iterate through the sorted items, adding as many units as possible
    for weight, value_per_unit in items_list:
        units_to_add = min(weight, remaining_capacity)
        total_value += units_to_add * value_per_unit
        remaining_capacity -= units_to_add

    return int(total_value)

items = {1: (10, 60), 2: (20, 100), 3: (30, 120)}
C = 50
print(MaxvalueSelection(items, C))  # Output: 240

