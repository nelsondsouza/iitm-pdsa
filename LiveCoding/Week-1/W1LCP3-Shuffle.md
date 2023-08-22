Write a function  **shuffle(l1,l2)**  that takes two lists,  `l1`  and  `l2`  as input, and returns a list consisting of the first element in  `l1`, then the first element in  `l2`, then the second element in  `l1`, then the second element in  `l2`, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.  
  

**Sample Input**

```
[0,2,4]
[1,3,5]
```

**Output**

```python
[0, 1, 2, 3, 4, 5]
```

**Sample Input**

```
[0,2,4]
[1]
```

**Output**

```python
[0, 1, 2, 4]
```
```python
def shuffle(l1, l2):
    result = []
    length = max(len(l1), len(l2))

    for i in range(length):
        if i < len(l1):
            result.append(l1[i])
        if i < len(l2):
            result.append(l2[i])

    return result

L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
```
