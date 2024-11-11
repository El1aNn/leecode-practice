from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # @cache
        # def dfs(i, k, hold):
        #     if k < 0:
        #         return -inf
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i - 1, k - 1, 0) - prices[i], dfs(i - 1, k, 1))
        #     else:
        #         return max(dfs(i - 1, k, 1) + prices[i], dfs(i - 1, k, 0))
        # return dfs(n - 1, 2, 0)
        dp = [[-inf] * 2 for _ in range(3)]
        dp[0][0] = 0
        for x in prices:
            for k in range(2):
                dp[k+1][1] = max(dp[k+1][1], dp[k][0] - x)
                dp[k+1][0] = max(dp[k+1][0], dp[k+1][1] + x)
        return dp[2][0]