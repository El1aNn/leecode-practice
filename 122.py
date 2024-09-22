# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润 。
from cmath import inf
from functools import cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i - 1, 1), dfs(i - 1, 0) - prices[i])
        #     return max(dfs(i - 1, 0), dfs(i - 1, 1) + prices[i])
        #
        # return dfs(n - 1, 0)
        dp = [[0] * 2 for _ in range(n + 1)]

        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][1], dp[i][0] - p)
            dp[i + 1][1] = max(dp[i][0], dp[i][1] + p)
        return dp[-1][0]


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
