![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/b5849ae6-afff-4d9f-91f2-946ce758c90d)

```python
def pickingNumbers(a):
    a.sort()
    count = 1
    pos = 0
    maxx = 0
    for i in range(1, len(a)):
        if abs(a[i] - a[pos]) <= 1:
            count = count + 1
        else:
            if count > maxx:
                maxx = count
            count = 1
            pos = i
    if maxx > count:
        return maxx
    else:
        return count

a=[int(item) for item in input().split(" ")]
print(pickingNumbers(a))
```
