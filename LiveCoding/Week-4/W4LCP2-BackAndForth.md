![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L3.1.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L3.2.png)
```python
def BFSListPath(AList, v, preventionList):
    visited, parent = {}, {}
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = []
    visited[v] = True
    q.append(v)
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if not visited[k] and k not in preventionList:
                visited[k] = True
                parent[k] = j
                q.append(k)
    return visited, parent

def findpath(parent, start, end):
    L = []
    curr = parent[end]
    while curr != start:
        L.append(curr)
        curr = parent[curr]
    return L

def backandforth(AList, end1, end2):
    preventionList = []
    c = 0
    visited, parent = BFSListPath(AList, end1, preventionList)
    while visited[end2]:
        c += 1
        path = findpath(parent, end1, end2)
        preventionList.extend(path)
        visited, parent = BFSListPath(AList, end1, preventionList)
    return c

end1 = int(input())
end2 = int(input())

AList = {}

while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)

print(backandforth(AList, end1, end2))
```
