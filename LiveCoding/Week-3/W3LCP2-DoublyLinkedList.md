![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W3P2.JPG)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W3P2.1.JPG)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
      
    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:            
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    def insert_at_pos(self, data, pos):
        newnode = Node(data)
        c = 1
        temp = self.head
        while c < pos - 1:
            temp = temp.next
            c += 1
        temp1 = temp.next
        temp.next = newnode
        newnode.next = temp1
        newnode.prev = temp
        temp.next = newnode
        temp1.prev = newnode
```
