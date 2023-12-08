'''
Minimize cost to reach the destination

You are given a grid of size m x n with positive integer values representing the cost you have to pay in each cell. You can only jump either one cell down or one cell right at a point in time. Your goal is to find the minimum cost to reach the bottom-right corner cell (m-1, n-1) of the grid, starting from the top-left corner cell (0, 0).

Write a function min_cost(m, n, grid_costs) that takes in two integers m and n representing the number of rows (indexed from 0 to m-1) and the number of columns (indexed from 0 to n-1), and a 2D nested list grid_costs representing the cost of each cell.

The function should return an integer indicating the minimum cost to reach the bottom-right corner cell (m-1, n-1) of the grid starting from the top-
left corner cell (0, 9).

Sample Input 1
3 #m
3 #n
[[1, 3, 1],[1, 5, 1],[4, 2, 1]] #grid_costs

Output
7

Explanation
[[1, 3, 1],
[1, 5, 1],
[4, 2, 1]]
The minimum cost path is 1(@,@) -> 3(@,1) -> 1(@,2) -> 1(1,2) -> 1(2,2), with a total cost of 7.

Sample Input 2
3
3
[[1, 3, 2],[1, 2, 4],[4, 1, 1]]

Output
6

Explanation
[[1, 3, 2],
[1, 2, 4],
[4, 1, 1]]
The minimum cost path is 1(@,@) -> 1(1,@) -> 2(1,1) -> 1(2,1) -> 1(2,2), with a total cost of 6.

'''

def min_cost(m, n, grid_costs):
    # Create a 2D array to store the minimum cost to reach each cell
    dp = [[0] * n for _ in range(m)]

    # Initialize the first cell
    dp[0][0] = grid_costs[0][0]

    # Initialize the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid_costs[0][j]

    # Initialize the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid_costs[i][0]

    # Fill the rest of the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid_costs[i][j] + min(dp[i-1][j], dp[i][j-1])

    # Return the minimum cost to reach the bottom-right corner
    return dp[m-1][n-1]

# Sample Input 1
m1 = 3
n1 = 3
grid_costs1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

# Sample Input 2
m2 = 3
n2 = 3
grid_costs2 = [[1, 3, 2], [1, 2, 4], [4, 1, 1]]

# Output
output1 = min_cost(m1, n1, grid_costs1)
output2 = min_cost(m2, n2, grid_costs2)

print("Output 1:", output1)  # Output 1: 7
print("Output 2:", output2)  # Output 2: 6
