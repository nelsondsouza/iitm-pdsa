![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/296482ee-ae0a-4f06-a098-6cfb33a3ec7c)

```python
def median(A, B, sA, lA, sB, lB):
    n = lA - sA + 1
    mid = n // 2
    midA = sA + mid
    if n % 2 == 0:
        midB = sB + mid - 1
    else:
        midB = sB + mid
    if n == 1:
        return (A[sA] + B[sB]) / 2
    elif n == 2:
        return (max(A[sA], B[sB]) + min(A[lA], B[lB])) / 2
    elif A[midA] == B[midB]:
        return (A[midA] + B[midB]) / 2
    elif A[midA] > B[midB]:
        return median(A, B, sA, midA, midB, lB)
    elif A[midA] < B[midB]:
        return median(A, B, midA, lA, sB, midB)

def findMedian(A, B):
    return median(A, B, 0, len(A) - 1, 0, len(B) - 1)
```
