You are given a network of n nodes, labelled from 0 to n-1. You are also given travel_times, a list of signal travel times in as directed edges travel_times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

Write a function min_transmission_time(n, travel_times, s) that accept number of nodes n, a list travel_times and a source node s to send the signal . The function returns the minimum time required for the signal sent by the source node s to be received by all the remaining n-1 nodes. If it is impossible to obtain a signal for all n-1 nodes, return -1.

**Sample Input 1**
```
4 #n
[(1,0,1),(1,2,1),(2,3,1)] #travel_times
2 #s
```
**Output**
```
2
```
 
**Sample Input 2**
```
4
[(1,0,1),(1,2,1),(3,2,1)]
2
```

**Output**
```
-1
```

**Sample Input 3**
```
7
[(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
0
```

**Output**
```
86
```
```python
def dijkstralist(WList, s):

  infinity = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v, d) in WList[u]])
  (visited, distance) = ({}, {})
  for v in WList.keys():
    (visited[v], distance[v]) = (False, infinity)
  distance[s] = 0

  for _ in range(len(WList.keys())):
    nextd = min([distance[v] for v in WList.keys() if not visited[v]])
    nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
    nextv = min(nextvlist)
    visited[nextv] = True
    for (v, d) in WList[nextv]:
      if not visited[v]:
        distance[v] = min(distance[v], distance[nextv] + d)

  return (distance, infinity)

def min_transmission_time(n, travel_times, s):

  AList = {}
  for i in range(n):
    AList[i] = []
  for u, v, d in travel_times:
    AList[u].append((v, d))

  dist, inf = dijkstralist(AList, s)
  maxtime = 0
  for node, distance in dist.items():
    if distance >= maxtime:
      maxtime = distance

  if maxtime >= inf:
    return -1
  else:
    return maxtime
n = int(input())
edges = eval(input())
s = int(input())
print(min_transmission_time(n, edges, s))
```
