class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        # @cache
        # def dfs(i, j):
        #     if j < 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if s[i] == t[j]:
        #         return dfs(i - 1, j) + dfs(i - 1, j - 1)
        #     return dfs(i - 1, j)
        # return dfs(m - 1, n - 1)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]
