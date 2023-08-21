'''
Domino Solitaire

In Domino Solitaire, you have a grid with two rows and many columns. Each square in the grid
contains an integer. You are given a supply of rectangular 2 x 1 tiles, each of which exactly covers
two adjacent squares of the grid. You have to place tiles to cover all the squares in the grid such
that each tile covers two squares and no pair of tiles overlap. The score for a tile is the difference
between the bigger and the smaller number that are covered by the tile. The aim of the game is to
maximize the sum of the scores of all the tiles. 

Your task is to read the grid of numbers and compute the maximum score that can be achieved by any tiling of the grid.

Solution hint
Recursively find the best tiling, from left to right. You can start the tiling with one vertical tile or two horizontal tiles. Use dynamic programming to evaluate the recursive expression efficiently.

Input format
The first line contains one integer N, the number of columns in the grid. This is followed by 2 lines describing the grid. Each of these lines consists of N integers, separated by blanks.
'''

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
