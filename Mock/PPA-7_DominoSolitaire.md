![](https://backend.seek.onlinedegree.iitm.ac.in/21t3_cs2002/assets/img/domi.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/21t3_cs2002/assets/img/dom.png)
```python
n = int(input())
arr = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

prev_state = 0
final = abs(arr[0] - arr_2[0])

for i in range(1, n):
    vertical_place = final + abs(arr[i] - arr_2[i])
    horizontal_place = prev_state + abs(arr[i] - arr[i-1]) + abs(arr_2[i] - arr_2[i-1])
    prev_state = final
    final = max(vertical_place, horizontal_place)

print(final)
```
