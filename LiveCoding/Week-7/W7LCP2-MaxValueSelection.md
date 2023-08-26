![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/178fadca-bc0f-4816-bdb4-56ab4e2482ad)

```python
def MaxValueSelection(items, C):
    itemlist = []
    for i, j in items.items():
        itemlist.append((j[1] / j[0], i, j[0]))
    itemlist.sort(reverse=True)

    maxvalue = 0
    for itm in itemlist:
        if C > itm[2]:
            maxvalue += itm[0] * itm[2]
            C -= itm[2]
        else:
            maxvalue += C * itm[0]
            C = 0
            break

    return maxvalue

items = eval(input())
C = int(input())
print(round(MaxValueSelection(items, C),2))
```
