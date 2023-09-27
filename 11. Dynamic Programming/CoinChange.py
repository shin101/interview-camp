from typing import List

# Coin Change - Print Count: Given a set of coin denominations, print out the number of ways you can make a target amount. You can use as many coins of each denomination as you like.

# For example: If coins are [1,2,5] and the target is 5, the different ways are:
# [1,1,1,1,1]
# [1,1,1,2]
# [1,2,2]
# [5]
# The Output will be 4.


        # amount + 1 is the default 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        
        return dp[amount] if dp[amount]!=float('inf') else -1 
