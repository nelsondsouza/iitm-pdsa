'''Find Number of Occurrence
Write a function findOccurrence(L,k) that accepts an unsorted list L of integers and an integer k.
The function returns the total number of occurrences of k in the list L.  If k is not present in the list then return -1.
Write an efficient solution of complexity O(n)

Sample Input
[1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,3,3,3]
3
Sample Output
9'''

def findOccurrence(L, k):
    count = 0
    
    for num in L:
        if num == k:
            count += 1
    
    if count == 0:
        return -1
    
    return count

# Sample Input
L = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 5, 5, 3, 3, 6, 3, 4, 3]
k = 3

# Calculate and print the output
output = findOccurrence(L, k)
print("Number of occurrences of", k, ":", output)
