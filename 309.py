from math import inf
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        dp = [0] * 2
        dp[1] = -float('inf')
        pre = 0
        for p in prices:
            tmp = dp[0]  # 保存未更新的 dp[0]
            dp[0] = max(dp[0], dp[1] + p)
            dp[1] = max(dp[1], pre - p)
            pre = tmp  # 更新 pre 为原始的 dp[0]
        return dp[0]
    def maxProfit2(self, prices: List[int]) -> int:
        dp = [0] * 2
        pre = 0
        dp[1] = -inf
        for p in prices:
            pre, dp[0], dp[1] = dp[0], max(
                dp[0], dp[1] + p), max(dp[1], pre - p)
        return dp[0]


s = Solution()
print(s.maxProfit1([1, 2, 3, 0, 2]))
print(s.maxProfit2([1, 2, 3, 0, 2]))
