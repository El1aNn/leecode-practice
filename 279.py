# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e9 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, int(sqrt(n))):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)

        return dp[-1]


s = Solution()
print(s.numSquares(12))
