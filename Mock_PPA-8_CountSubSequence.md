![](https://backend.seek.onlinedegree.iitm.ac.in/22t2_cs2002/assets/img/pdsaactq2i1.png)

```python

def countSubseq(s):
    max_subseq = [0] * 10  # Initialize a list to track maximum subsequences for each digit
    
    for char in s:
        num = int(char)  # Convert the character to a number
        new_subseq = 1 + sum(max_subseq[:num])  # Calculate new subsequences
        max_subseq[num] += new_subseq  # Update max_subseq for this digit
    
    return sum(max_subseq)
S = input()
print(countSubseq(S))

```
