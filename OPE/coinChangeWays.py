'''Coin Change Ways

You are given a set of coins, each with a different positive denomination, and a target amount of money. 
Your task is to determine the number of distinct ways you can make up the target amount using the given coins. 
You have an infinite supply of each coin denomination.

Implement a function coin_change_ways(coins, amount) that takes in a list of coin denominations "coins" and an integer "amount", 
and returns the number of distinct ways to make up the amount using the given coins.

Sample input 1
1, 2, 5
5

Output:
4

Explanation
There are four ways to make up the amount 5: [1, 1, 1, 1, 1, [1, 1, 1, 2), {1, 2, 2), and [5].

Sample Input 2
[2, 3, 4, 7]
7

Output:
3

Explanation
There are three ways to make up the amount 7: [2, 2, 3], [3, 4], and [7].
'''

def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Test the function with the given samples
print(coin_change_ways([1, 2, 5], 5))  # Output: 4
print(coin_change_ways([2, 3, 4, 7], 7))  # Output: 3