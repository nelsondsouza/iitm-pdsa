![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/bea83825-e8f4-4542-ba8c-23d3619c54ab)

```python
def cutRod(n, price):
    length = []
    st = [[0 for i in range(n + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        length.append(i)
        
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if length[i - 1] <= j:
                st[i][j] = max(price[i - 1] + st[i][j - length[i - 1]], st[i - 1][j])
            else:
                st[i][j] = st[i - 1][j]
                
    return st[n][n]

N = int(input())
price= eval(input())
print(cutRod(N,price))
```
