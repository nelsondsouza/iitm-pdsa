![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/w1lc8.png)
```python
def Max_Amount(list):
    min_val = min(list)
    max_val = max(list)
    if min_val == list[0] or max_val == list[-1]:
        return max_val - min_val
    else:
        max_diff = max(max(list) - list[0], list[-1] - min(list), max([list[i] - list[i+1] for i in range(len(list) - 1)]), list[-1] - list[0])
        return max_diff
```
