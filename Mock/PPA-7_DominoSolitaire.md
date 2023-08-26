![](https://backend.seek.onlinedegree.iitm.ac.in/21t3_cs2002/assets/img/domi.png)
![](https://backend.seek.onlinedegree.iitm.ac.in/21t3_cs2002/assets/img/dom.png)

## [Visualization](https://cscircles.cemc.uwaterloo.ca/visualize#code=n+%3D+int(input())%0Aarr+%3D+list(map(int,+input().split()))%0Aarr_2+%3D+list(map(int,+input().split()))%0A%0Aprev_state+%3D+0%0Afinal+%3D+abs(arr%5B0%5D+-+arr_2%5B0%5D)%0A%0Afor+i+in+range(1,+n)%3A%0A++++vertical_place+%3D+final+%2B+abs(arr%5Bi%5D+-+arr_2%5Bi%5D)%0A++++horizontal_place+%3D+prev_state+%2B+abs(arr%5Bi%5D+-+arr%5Bi-1%5D)+%2B+abs(arr_2%5Bi%5D+-+arr_2%5Bi-1%5D)%0A++++prev_state+%3D+final%0A++++final+%3D+max(vertical_place,+horizontal_place)%0A%0Aprint(final)&mode=display&raw_input=4%0A8+6+2+3%0A9+7+1+2&curInstr=9)


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
