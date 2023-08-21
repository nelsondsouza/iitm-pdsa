![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m1.png)![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m1.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m1.png)![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m2.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m1.png)![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m3.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m3.png)![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/m4.png)
```python
import copy
def dijkstra(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)       
    distance[s] = 0    
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)        
        visited[nextv] = True        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if distance[v] > distance[nextv] + d:
                    distance[v] = distance[nextv] + d   
    return(distance)
def shortestCircularRoute(WList, s):
    shortest_route = float('inf')
    for (neighbor, distance_to_neighbor) in WList[s]:
        temp_WList = copy.deepcopy(WList)
        temp_WList[s].remove((neighbor, distance_to_neighbor))
        temp_WList[neighbor].remove((s, distance_to_neighbor))
        distance = dijkstra(temp_WList, neighbor)
        if s in distance and distance[s] + distance_to_neighbor < shortest_route:
            shortest_route = distance[s] + distance_to_neighbor
    return shortest_route
n = int(input())
edges = eval(input())
S = int(input())
WL = {}
for i in range(n):
    WL[i] = []
for ed in edges: #create dictionary for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(shortestCircularRoute(WL,S))
```
