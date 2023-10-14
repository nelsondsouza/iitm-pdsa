![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/W3LC1NN.png)
```python
def removeDuplicate(head):
    if head is None:
        return None
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
```
