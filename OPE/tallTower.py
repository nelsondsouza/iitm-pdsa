""" 
Tall Tower
A tower is built using a combination of cylinders of different diameters and heights. We have to build a tall tower by placing one cylinder over another. The constraint is that in each adjacent pair of cylinder in tower, the top cylinder diameter should be less than or equal to the bottom cylinder diameter, and the volume of the top cylinder should be at most half the volume of the bottom cylinder. Each cylinder has a unique id starting from 0 to n-1, where n is the number of cylinders available.
Write a function tallTower(L) that accepts a list L of tuples and returns the maximum height achieved by stacking the cylinders. The tuples in the list L have the values (id, diameter, height).
Formula
Volume of cylinder = 3.14 * (Diameter/2)^2 * Height

Sample input
[(0, 2, 2), (1, 3, 7), (2, 5, 6), (3, 1, 5), (4, 10, 1)]
Sample Output
9

# You can use the following ‘tuplesort’ function to sort the list by particular ‘index’ if required.
def tuplesort(L, index):
	L_= []
	for t in L:
		L_.append(t[index:index+1] + t[:index] + t[index+1:])
	L_.sort()
	L__= []
	for t in L_:
		L__.append(t[1:index+1] + t[0:1] + t[index+1:])
	return L__ 
    """


def tallTower(L):
    # Sort the cylinders in descending order of their diameters
    L.sort(key=lambda x: x[1], reverse=True)

    # Initialize a list to store the maximum heights achieved for each cylinder
    max_heights = [0] * len(L)

    # Iterate over each cylinder
    for i in range(len(L)):
        # Get the id, diameter, and height of the current cylinder
        curr_id, curr_diameter, curr_height = L[i]

        # Initialize the maximum height for the current cylinder with its own height
        max_heights[curr_id] = curr_height

        # Iterate over the previous cylinders
        for j in range(i):
            # Get the id, diameter, and height of the previous cylinder
            prev_id, prev_diameter, prev_height = L[j]

            # Check if the current cylinder can be placed on top of the previous cylinder
            if curr_diameter <= prev_diameter and curr_height <= prev_height * 0.5:
                # Update the maximum height for the current cylinder if a higher height is achieved
                max_heights[curr_id] = max(max_heights[curr_id], curr_height + max_heights[prev_id])

    # Return the maximum height achieved among all cylinders
    return max(max_heights)

# Sample input
cylinders = [(0, 2, 2), (1, 3, 7), (2, 5, 6), (3, 1, 5), (4, 10, 1)]
print(tallTower(cylinders))  # Output: 9


