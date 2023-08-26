![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/10bb3db2-298c-429d-b727-ae1e4ab8dd06)

```python
def solvem(n, height, memo):
    if memo[n] == -1:
        if n == 0:
            ans = 0
        elif n == 1:
            ans = abs(height[1] - height[0])
        elif n > 1:
            ans = min(
                solvem(n - 1, height, memo) + abs(height[n] - height[n - 1]),
                solvem(n - 2, height, memo) + abs(height[n] - height[n - 2])
            )
        memo[n] = ans
    return memo[n]

def minCost(H):
    memo = {}
    for i in range(len(H)):
        memo[i] = -1
    return solvem(len(H) - 1, H, memo)


H = eval(input())
print(minCost(H))
```
