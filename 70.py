from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        # d = {}
        # d[1] = 1
        # d[2] = 2
        # for i in range(1, n + 1):
        #     if i not in d:
        #         d[i] = d[i - 1] + d[i - 2]
        #
        # return d[n]
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     if i == 1:
        #         return 2
        #     res = dfs(i - 1) + dfs(i - 2)
        #     return res
        @cache
        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            if i == 1:
                return 2
            res = dfs(i - 1) + dfs(i - 2)
            return res

        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
