![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Live%20W1.P4.png)

```python
def expanding(L):
    if len(L) < 3:
        return True

    prev_diff = abs(L[1] - L[0])
    for i in range(2, len(L)):
        curr_diff = abs(L[i] - L[i-1])
        if curr_diff <= prev_diff:
            return False
        prev_diff = curr_diff

    return True

L = eval(input())
print(expanding(L))
```
