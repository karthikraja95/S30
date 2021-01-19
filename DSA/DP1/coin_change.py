"""
O(S*N) where S is amount between 1<=i<=S
where N is no of coin denomination

O(S+N) extra space for dp table

initialise dp table as list of list and assign inf
or higher value to Ast row and for 0 to amount columns

if the curr amt less than denomination , copy the
previous row same col value

else find min between (prev value,1+dp[i][j-curr_denomination]

if value gt than 9999 or Inf return -1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0:
            return 0
        dp = [
            [0 for i in range(amount + 1)] for j in range(len(coins) + 1)
        ]  # integer overflow is handled in pytho so we can put infinity or 9999 or amount+1
        dp[0] = [9999] * (amount + 1)
        dp[0][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
        if dp[len(coins)][amount] >= 9999:
            return -1
        else:
            return dp[len(coins)][amount]  # last row last column


#         RECURSIVE - TLE
#         def helper(coins, amount, index, minCoins):
#             if amount == 0:
#                 return minCoins

#             if amount < 0 or index >= len(coins):
#                 return -1

#             #choose coin at index
#             choose = helper(coins, amount - coins[index], index, minCoins+1)
#             #don't choose coin at index
#             dontChoose = helper(coins, amount, index + 1, minCoins)

#             if choose == -1:
#                 return dontChoose
#             elif dontChoose == -1:
#                 return choose

#             return min(choose, dontChoose)

#         return helper(coins, amount, index=0, minCoins=0)
