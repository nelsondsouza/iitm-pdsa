![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L2.1.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L2.2.png)
```python
def BFSListPathLevel(AList, v):
    level, parent = {}, {}
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = []
    level[v] = 0
    q.append(v)
    while len(q) > 0:
        j = q.pop(0)
        for k in AList[j]:
            if level[k] == -1:
                level[k] = level[j] + 1
                parent[k] = j
                q.append(k)
    return level, parent

def minimumhops(AList, start, end):
    level, path = BFSListPathLevel(AList, start)
    shortestpath = []
    if level[end] != -1:
        shortestpath.append(end)
        while shortestpath[-1] != start:
            end = path[end]
            shortestpath.append(end)
    else:
        shortestpath.append(start)
    return shortestpath[::-1]
start = int(input())
end = int(input())
AList = eval(input())
shortestpath = minimumhops(AList, start, end)
print(len(shortestpath))
```
