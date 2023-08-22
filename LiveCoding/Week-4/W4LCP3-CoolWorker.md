![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L4.1.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W4L4.2.png)

```python
def coolWorkers(AList, preference):
    n = len(AList.keys())
    indegree = {}
    toposortlist = []
    
    for i in AList.keys():
        indegree[i] = 0
    
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    for i in range(n):
        availableTasks = [k for k in AList if indegree[k] == 0]
        t = [(preference.index(i), i) for i in availableTasks]
        t.sort()
        j = t[0][1]
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] -= 1
    
    return toposortlist

AList = eval(input())
preference = eval(input())
print(coolWorkers(AList, preference))
```
