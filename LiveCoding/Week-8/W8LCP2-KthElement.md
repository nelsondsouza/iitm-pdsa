![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/a4bd3d4c-dd63-4766-9ef3-828ccc2635ec)

```python
def kth(arr1, arr2, n, m, k):
    if n == 1 or m == 1:
        if m == 1:
            arr2, arr1 = arr1, arr2
            n, m = m, n
        if k == 1:
            return min(arr1[0], arr2[0])
        elif k == m + n:
            return max(arr1[0], arr2[m - 1])
        else:
            if arr2[k - 2] > arr1[0]:
                return arr2[k - 2]
            else:
                return min(arr1[0], arr2[k - 1])

    mid1 = (n - 1) // 2
    mid2 = (m - 1) // 2

    if k > mid1 + mid2 + 1:
        if arr1[mid1] < arr2[mid2]:
            return kth(arr1[mid1 + 1:], arr2, n - mid1 - 1, m, k - mid1 - 1)
        else:
            return kth(arr1, arr2[mid2 + 1:], n, m - mid2 - 1, k - mid2 - 1)
    else:
        if arr1[mid1] < arr2[mid2]:
            return kth(arr1, arr2[:mid2 + 1], n, mid2 + 1, k)
        else:
            return kth(arr1[:mid1 + 1], arr2, mid1 + 1, m, k)

def KthElement(A, B, k):
    return kth(A, B, len(A), len(B), k)
```
