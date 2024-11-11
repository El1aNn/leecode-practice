from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+2) for _ in range(m)]
        for i in range(m):
            dp[i][0] = dp[i][-1] = float('inf')
        for i in range(n):
            dp[0][i+1] = matrix[0][i]
        for i in range(1, m):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j],
                               dp[i-1][j+1]) + matrix[i][j-1]
        return min(dp[-1])
