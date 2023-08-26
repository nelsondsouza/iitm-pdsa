![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/1580ca2c-bb42-478d-bc1b-a5d1483d585c)

```python
def knapSack(W, weight, value, N):
    st = [[0 for i in range(W + 1)] for j in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if weight[i - 1] <= j:
                st[i][j] = max(value[i - 1] + st[i - 1][j - weight[i - 1]], st[i - 1][j])
            else:
                st[i][j] = st[i - 1][j]
                
    return st[N][W]

N=int(input())
W=int(input())
weight=eval(input())
values=eval(input())
print(knapSack(W,weight,values,N))
```
