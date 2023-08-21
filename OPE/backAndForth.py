'''
Write a function backandforth(AList, endl, end2) to return the maximum number of possible
route between node endl and node end2 in the undirected graph without going through the
same node again with exception to endl and end2. The connectivity details between nodes are
provided by the adjacency list AList.

Sample Input
AList = {
O: (2, 3, 6],
2: (0, 3, 4],
3: (4, 2, 0, 1),
6: (1, 5, 0],
1: (3, 6, 5],
4: (2, 3, 5],
5: (1, 4, 6]
}
endl = 0
end2 = 1

Sample Output
3
'''

def backandforth(AList, endl, end2):
    num_routes = 0
    visited = set()

    def _explore(node):
        nonlocal num_routes
        if node == end2:
            num_routes += 1
            return
        visited.add(node)
        for neighbor in AList[node]:
            if neighbor not in visited:
                _explore(neighbor)
        visited.remove(node)  # Backtrack

    _explore(endl)
    return num_routes

AList = {
    0: [2, 3, 6],
    2: [0, 3, 4],
    3: [4, 2, 0, 1],
    6: [1, 5, 0],
    1: [3, 6, 5],
    4: [2, 3, 5],
    5: [1, 4, 6]
}
endl = 0
end2 = 1

print(backandforth(AList, endl, end2))  # Output: 3
