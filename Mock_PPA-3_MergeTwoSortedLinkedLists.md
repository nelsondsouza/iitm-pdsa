![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/mockppa2.png)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedList(head1, head2):
    dummy = Node(0)
    current = dummy

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1 is not None:
        current.next = head1
    else:
        current.next = head2

    return dummy.next

# Sample input: creating the linked lists
elements1 = [1, 3, 5, 7, 9, 11]
head1 = Node(elements1[0])
current = head1
for element in elements1[1:]:
    current.next = Node(element)
    current = current.next

elements2 = [2, 4, 6]
head2 = Node(elements2[0])
current = head2
for element in elements2[1:]:
    current.next = Node(element)
    current = current.next

# Call the function to merge the sorted linked lists
merged_head = mergeSortedList(head1, head2)
```
