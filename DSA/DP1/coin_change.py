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
