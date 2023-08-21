![](https://backend.seek.onlinedegree.iitm.ac.in/23t1_cs2002/assets/img/mock1jan2023.png)

```python
def minmax(a, b):
    # Go through each pair of elements in the two lists
    for i in range(len(a)):
        # If the element in list a is less than the element in list b, swap them
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
    # Find the maximum value in each list and return their product
    return max(a) * max(b)
a = eval(input())
b = eval(input())
print(minmax(a,b))
```
