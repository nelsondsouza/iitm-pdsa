![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/W2P3.1.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/22t1_cs2002/assets/img/Screenshot%20from%202021-12-29%2015-49-54.png)
```python
def merge(deck1, deck2):
    merged_deck = []
    i = j = 0
    while i < len(deck1) and j < len(deck2):
        if deck1[i] < deck2[j]:
            merged_deck.append(deck1[i])
            i += 1
        else:
            merged_deck.append(deck2[j])
            j += 1
    while i < len(deck1):
        merged_deck.append(deck1[i])
        i += 1
    while j < len(deck2):
        merged_deck.append(deck2[j])
        j += 1
    return merged_deck

def subordinates(L):
    if len(L) <= 2:
        return sorted(L), 1
    
    mid = len(L) // 2
    left_deck, left_people = subordinates(L[:mid])
    right_deck, right_people = subordinates(L[mid:])
    sorted_deck = merge(left_deck, right_deck)
    
    return sorted_deck, left_people + right_people + 1

print(subordinates(eval(input())))
```
