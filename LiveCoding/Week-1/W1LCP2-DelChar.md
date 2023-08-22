![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Live%20W1.P2.png)

```python

def del_char(s, c):
    if len(c) != 1:
        return s

    result = ""
    for char in s:
        if char != c:
            result += char

    return result

s = input()
c = input()
print(del_char(s,c))

```
