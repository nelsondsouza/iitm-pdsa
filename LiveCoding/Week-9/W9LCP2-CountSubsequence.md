![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/cf6728c5-7b47-41a6-b4c6-c549478f27c6)

```python
def countSubseq(S):
    L = []
    n = len(S)
    for d in S:
        L.append(int(d))
    count = [0 for i in range(10)]
    
    for i in range(n):
        for j in range(L[i] - 1, -1, -1):
            count[L[i]] += count[j]
        count[L[i]] += 1
        
    result = 0
    for i in range(10):
        result += count[i]
        
    return result

#Suffix Code
S = input()
print(countSubseq(S))
```
