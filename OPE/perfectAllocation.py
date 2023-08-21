'''
Minimize the maximum allocation
A hospital is digitizing its old patients’ manual records for a newly purchased ERP software.
There are m registers such that register i has b_i patient records. There are k persons available to
perform data entry for the m registers, where k <= m. Each register will be allocated to exactly
one person. Each person has to be allocated at least one register for entry.
The time each person takes to enter a register's data is directly proportional to the number of
patient records in the register. The goal is to parallelize the entry process to finish in the fastest
possible time. For this, we need to allocate registers in contiguous order such that the maximum
number of patient records assigned to any one person is minimized.
Write a function perfectAllocation(m, k) that accepts a list m which contains positive integers as
elements where each ith element in the list represents the number of patient records in the ith
register and k represents the number of persons available for data entry. Out of all allocations,
the task is to find that particular allocation in which the maximum number of patient records
allocated to a person is the least compared to all other possible allocations.

Sample Input
[100,200,300,400,500,600,700,800,900] # m
3 #k

Output
1700
'''

def is_valid(mid, m, k):
    persons_required = 1
    current_sum = 0

    for i in m:
        if i > mid:
            return False
        current_sum += i
        if current_sum > mid:
            persons_required += 1
            current_sum = i

    return persons_required <= k

def perfectAllocation(m, k):
    low = max(m)
    high = sum(m)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid, m, k):
            result = min(result, mid)
            high = mid - 1
        else:
            low = mid + 1

    return result

m = [100,200,300,400,500,600,700,800,900]
k = 3
print(perfectAllocation(m, k))  # Output: 1700
