![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Live%20W1.P6.png)

```python
def histogram(l):
    freq = {}
    for num in l:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = [(num, freq[num]) for num in sorted(freq, key=lambda x: (freq[x], x))]
    return result

L=eval(input())
print(histogram(L))
```
