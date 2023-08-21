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
    def binarySearch(nums, target, searchFirst):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                result = mid

                if searchFirst:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return result

    first = binarySearch(L, k, True)
    last = binarySearch(L, k, False)

    if first != -1:
        return last - first + 1
    else:
        return -1

# Sample Input
L = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4]
k = 3

# Calculate and print the output
output = findOccurrence(L, k)
print("Number of occurrences of", k, ":", output)
