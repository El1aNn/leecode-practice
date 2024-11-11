from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])

        # @cache
        # def dfs(i, left):
        #     if i < 0:
        #         return abs(left)
        #     res = float('inf')
        #     for j in range(n):
        #         res = min(res, dfs(i - 1, left - mat[i][j]))
        #     return res
        # return dfs(m - 1, target)
        dp = [float('inf') for _ in range(target + 1)]
        for i in range(n):
            dp[i] = abs(target - mat[0][i])
        for i in range(1, m):
            for j in range(n):
                for k in range(target, -1, -1):
                    dp[k] = min(dp[k], dp[k - mat[i][j]])
        return min(dp)
