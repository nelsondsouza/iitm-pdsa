import matplotlib.pyplot as plt
import numpy as np

def MaxvalueSelection(items, C):
    items_list = [(weight, value / weight) for weight, value in items.values()]
    items_list.sort(key=lambda x: x[1], reverse=True)

    total_value = 0
    remaining_capacity = C
    selected_units = []
    total_values = []

    for weight, value_per_unit in items_list:
        units_to_add = min(weight, remaining_capacity)
        total_value += units_to_add * value_per_unit
        remaining_capacity -= units_to_add
        selected_units.append(units_to_add)
        total_values.append(units_to_add * value_per_unit)

    # Define the positions for the bars
    x = np.arange(len(selected_units))

    # Plotting the selected units and total values
    plt.bar(x - 0.2, selected_units, 0.4, label='Number of Units Selected')
    plt.bar(x + 0.2, total_values, 0.4, label='Total Value')

    plt.xlabel('Items')
    plt.ylabel('Value/Units')
    plt.title('Selected Units and Total Value for Each Item')
    plt.xticks(x, [f"Item {i+1}" for i in range(len(selected_units))])
    plt.legend()
    plt.show()

    return int(total_value)

items = {1: (10, 60), 2: (20, 100), 3: (30, 120)}
C = 50
print(MaxvalueSelection(items, C))  # Output: 240

