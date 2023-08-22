![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/W3LC3N.png)
```python
class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains reference to the next node if it exists, otherwise None

def mergeSortedList(head1, head2):
    dummyNode = Node(0)
    tail = dummyNode
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    return dummyNode.next
```
