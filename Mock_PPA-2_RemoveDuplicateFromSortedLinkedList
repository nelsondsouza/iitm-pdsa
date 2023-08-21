![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/W3LC1NN.png)

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicate(head):
    current = head
    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

# Sample input: creating the linked list
elements = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 7, 9]
head = Node(elements[0])
current = head
for element in elements[1:]:
    current.next = Node(element)
    current = current.next

# Call the function to remove duplicates
removeDuplicate(head)

```
