'''Find Number of Occurrence
Write a function findOccurrence(L,k) that accepts a sorted list L of integers and an integer k.
The function returns the total number of occurrences of k in the list L.  If k is not present in the list then return -1.
Write an efficient solution of complexity O(logn)
Note: Do not use slicing in solution code for the list because it is O(n) operation.

Sample Input
[1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4]
3
Sample Output
6'''

def findOccurrence(L, k):
    # Binary search to find the first occurrence of k
    left, right = 0, len(L) - 1
    first_occurrence = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if L[mid] == k:
            first_occurrence = mid
            right = mid - 1
        elif L[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    if first_occurrence == -1:
        return -1
    
    # Binary search to find the last occurrence of k
    left, right = first_occurrence, len(L) - 1
    last_occurrence = first_occurrence
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if L[mid] == k:
            last_occurrence = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return last_occurrence - first_occurrence + 1

# Sample Input
L = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4]
k = 3

# Calculate and print the output
output = findOccurrence(L, k)
print("Number of occurrences of", k, ":", output)
