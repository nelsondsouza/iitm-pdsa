![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/3b30285d-5aa3-445f-ab3c-aa375ce3512e)

```python
def kthlargest(root):
    global count, result
    if root.right != None:
        find_kth_largest(root.right, k)
        count += 1
        if count == k:
            result = root.value
            return
        find_kth_largest(root.left, k)
count = 0
result = -1

def find_kth_largest(root, k):
    kthlargest(root)
    return result
```
