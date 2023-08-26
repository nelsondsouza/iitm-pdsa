Write a function findRedundantEdges(E,n) that accept an edge list E in increasing order of the edge weight where all edge weights are distinct and the number of vertices n (labeled from 0 to n-1) in a connected undirected graph and the function returns a list of redundant edges in increasing order of weight, so by removing these edges, the graph should remain connected with the minimum total cost of edges(minimum cost spanning tree). Try to write solution code of complexity O((E+V)logV).


Note - Selected edges tuples in the output list should be similar to input list edges tuples.

Hint- Union-find data structure


**Sample input**
```
4
[(0,1,10),(1,2,20),(2,3,30),(3,0,40),(1,3,50)]
```

**Output**
```
[(3, 0, 40), (1, 3, 50)]
```


```python
class MakeUnionFind:
    def __init__(self):
        self.components = {}
        self.members = {}
        self.size = {}

    def make_union_find(self, vertices):
        for vertex in range(vertices):
            self.components[vertex] = vertex
            self.members[vertex] = [vertex]
            self.size[vertex] = 1

    def find(self, vertex):
        return self.components[vertex]

    def union(self, u, v):
        c_old = self.components[u]
        c_new = self.components[v]
        # Always add a member in components which have greater size
        if self.size[c_new] >= self.size[c_old]:
            for x in self.members[c_old]:
                self.components[x] = c_new
                self.members[c_new].append(x)
            self.size[c_new] += 1
        else:
            for x in self.members[c_new]:
                self.components[x] = c_old
                self.members[c_old].append(x)
            self.size[c_old] += 1

def findRedundantEdges(E, n):
    st = MakeUnionFind()
    st.make_union_find(n)
    redlist = []
    for edge in E:
        if st.find(edge[0]) != st.find(edge[1]):
            st.union(edge[0], edge[1])
        else:
            redlist.append(edge)
    return redlist

n = int(input())
E=eval(input())
print(findRedundantEdges(E,n))
```
