![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/5a793c12-5ec7-43ab-8b4d-96b3ce81ed79)

![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/8bf853e9-5a8e-4e0c-9567-592f13d6e687)

```python
def addallpath(WList,u, d, visited, path,allpath):
  	visited[u]= True
  	path.append(u)
  	if u == d:
         L = path.copy()
         allpath.append(L)
  	else:
         for i in WList[u]:
             if visited[i[0]]== False:
                 addallpath(WList, i[0], d, visited, path, allpath)      	
  	path.pop()
  	visited[u]= False

# Following function returns a list of all paths from s to d
# Format of returned list:- [[s,...,d],[s,...,d],...]
def findallpath(WList,s,d):
    visited = {}
    allpath = []
    for v in WList.keys():
        visited[v] = False
    path = []
    addallpath(WList,s, d, visited, path,allpath)
    return(allpath)
def best_fare(flight_route, source, destination, k):
    L = findallpath(flight_route, source, destination)
    if L != []:
        cost = 1 + len(flight_route.keys()) * max([d for u in flight_route.keys() for (v, d) in flight_route[u]])
        route = []
        for pth in L:
            if len(pth) < k + 3:
                s = 0
                for i in range(0, len(pth) - 1):
                    for j in flight_route[pth[i]]:
                        if pth[i + 1] == j[0]:
                            s += j[1]
                if s < cost:
                    cost = s
                    route = pth
        if route != []:
            return (cost, route)
        else:
            return 'Not found'
    else:
        return 'Not found'

size = int(input())
edges = eval(input())
s = int(input()) 
d = int(input())
k = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
print(best_fare(WL,s,d,k))
```

