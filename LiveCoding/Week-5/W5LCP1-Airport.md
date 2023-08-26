![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/e8ff4bd8-ef71-499c-a979-b5f719a0ed95)

![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/ff846d9e-045c-4f73-a414-4678742bccda)

```PYTHON
def kruskal(WList):
  edges, component, TE = ([], {}, [])
  for u in WList.keys():
    edges.extend([(d, u, v) for (v, d) in WList[u]])
    component[u] = u
  edges.sort()

  for (d, u, v) in edges:
    if component[u] != component[v]:
      TE.append((u, v))
      c = component[u]
      for w in WList.keys():
        if component[w] == c:
          component[w] = component[v]
  return TE

def Airport(distance_map):

  R = kruskal(distance_map)
  S = 0
  for e in R:
    for ed in distance_map[e[0]]:
      if ed[0] == e[1]:
        S += ed[1]
  return S

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(Airport(WL))
```


