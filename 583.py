class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # @cache
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return j + 1 if i < 0 else i + 1
        #     if word1[i] == word2[j]:
        #         return dfs(i - 1, j - 1)
        #     return min(dfs(i - 1, j), dfs(i, j - 1)) + 1
        # return dfs(len(word1) - 1, len(word2) - 1)
        m = len(word1)
        n = len(word2)
        dp = [0] * (n + 1)
        for j in range(n + 1):
            dp[j] = j
        for i in range(m):
            pre = dp[0]
            for j in range(n):
                tmp = dp[j + 1]
                dp[j + 1] = pre + \
                    1 if word1[i] == word2[j] else min(dp[j + 1], dp[j]) + 1
                pre = tmp
        return dp[n]
