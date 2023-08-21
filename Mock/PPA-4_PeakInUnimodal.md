![](https://backend.seek.onlinedegree.iitm.ac.in/22t2_cs2002/assets/img/pmock21.png)
```python
def peak_unimodal(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left
```
