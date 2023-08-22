# 

**Challenging Problem**  
  
Given a wooden piece, a grid containing  **n**  rows and  **m**  columns, each 1 x 1 square containing  **O**  written inside it. You can cut the original or any other rectangular piece obtained during the cutting into two new pieces along the grid lines. You will obtain a certain number of rectangle pieces after doing the cutting.  
**1 x 1 is a square, you cannot treat it as a rectangle.** 
Your task is to design each rectangular piece obtained in such a way that any pair of adjacent cells have different symbols.  
  
Symbols :  **X**  and  **O**

  
What would be the minimum number of cells you need to put an  **X**  on in an  **n x m**  grid to achieve the desired result ?

**Example:-**  For n = 2 and m = 4, output is 3

![](https://backend.seek.onlinedegree.iitm.ac.in/23t2_cs2002/assets/img/w1lc7.png)

Write a function  **Min_X(n, m)**  that accept the number of rows  **n**  and number of columns  **m**  as input and returns the minimum number of cells you need to put an  **X**  on in an  **n x m**  grid to achieve the desired result.

**Sample Input 1**

```python
2 # n 
4 # m
```

**Output**

```
3
```

**Sample Input 2**

```python
3
1
```

**Output**

```
1
```

```python
def Min_X(x,y):
      from math import ceil
      return ceil(x*y/3)
```
