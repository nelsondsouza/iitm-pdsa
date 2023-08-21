"""Cities of the ancient country xyz are connected by two-way (bidirectional) roads, so that from any city you can get to any other city. 
The Sultan wants to divide the country into two separate connected areas by destroying only one road between two cities, 
so that from the city of one area it is impossible to get to the city of another area. 
He asked the minister of transportation to find the list of single roads between two cities, 
so that by destroying any one of them, the country can be divided into two separate connected areas.

Write a function findBridgeRoads(n, roads) that accepts an integer n which represents the number of cities labeled from 0 to n-1 
and a list of tuples roads({(i,j)....]) where each tuple (i, j) represents the road between cities i and j. 
The function returns the list of roads [(p, q),..} in any order but in each road (p,q) inlist, p should be less than q, 
so by destroying any one of them, the country should be divided into two separate connected areas, 
each of size between 1 and n-1 including value 1 and n-1. 
If there are no roads which can divide the country into separate connected areas, then return an empty list.

Note:- You can use BFSList function given in prefix if required.

Sample input
6 #number of cities ‘n'
[(0,1),(1,2),(2,0),(3,4),(4,5),(3,5),(2,3)] # roads list between cities

Output
[(2,3)) #list of bridge road

Explanation
After destroying the road (2,3) one connected country (0,1,2,3,4,5) will be divided into two separate connected area (0,1,2) and (3,4,5)"""


def findBridgeRoads(n, roads):
    graph = [[] for _ in range(n)]
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    time = 0
    visited = [False] * n
    disc = [float("Inf")] * n
    low = [float("Inf")] * n
    parent = [-1] * n
    bridge_roads = []

    def bridgeUtil(u):
        nonlocal time
        children = 0
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        for v in graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                bridgeUtil(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridge_roads.append((min(u, v), max(u, v)))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]:
            bridgeUtil(i)

    return bridge_roads

# Sample Input
n = 6
roads = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (3, 5), (2, 3)]
output = findBridgeRoads(n, roads)
print("Output:", output)
