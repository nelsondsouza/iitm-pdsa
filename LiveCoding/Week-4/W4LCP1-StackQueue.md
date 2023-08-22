![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W3P4.JPG)
```python
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()
            
class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0
    def isempty(self):
        return self.size == 0

    def top(self):
        if not self.isempty():
            return self.q1.items[-1]
        else:
            return 'Stack is empty'

    def push(self, data):
        self.size += 1
        self.q2.enqueue(data)
        while self.q1.items != []:
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.isempty():
            self.size -= 1
            return self.q1.dequeue()
        else:
            return 'Stack is empty'
inp = eval(input())
dl = int(input())
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())
```
