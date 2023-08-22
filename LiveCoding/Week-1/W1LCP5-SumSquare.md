![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Live%20W1.P5.png)
```python
def sumsquare(l):
    odd_sum = 0
    even_sum = 0

    for num in l:
        square = num ** 2
        if num % 2 == 0:
            even_sum += square
        else:
            odd_sum += square

    return [odd_sum, even_sum]

L = eval(input())
print(sumsquare(L))
```
