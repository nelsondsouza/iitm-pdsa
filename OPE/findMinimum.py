""" 
Find Minimum
Write a function findMinimum(L) that accepts a non-empty sorted list of n distinct elements 
which has been shifted/rotated to the right or left an unknown number of times. 
For example, shifting [1, 2, 3, 4, 5] twice to the right results in [4, 5, 1, 2, 3] and 
shifting twice to the left results in [3, 4, 5, 1, 2]. The function returns the smallest element in the list L. 
Write an efficient solution of complexity O(logn).
Note:- Do not use slicing for the list because it is O(n) operation.

Sample Input
[5,6,7,8,9,1,2,3,4]
Output
l
"""

def findMinimum(L):
    left, right = 0, len(L) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If the element at mid is greater than the element at right, 
        # it means the minimum element is on the right side
        if L[mid] > L[right]:
            left = mid + 1
        else:
            # Otherwise, the minimum is on the left side
            right = mid

    return L[left]

# Sample input
print(findMinimum([5,6,7,8,9,1,2,3,4]))  # Output: 1
