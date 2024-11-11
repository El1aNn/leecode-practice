from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = [grid[i][j], grid[i][j]]
                elif i == 0:
                    dp[i][j] = [dp[i][j-1][0] * grid[i]
                                [j], dp[i][j-1][1] * grid[i][j]]
                elif j == 0:
                    dp[i][j] = [dp[i-1][j][0] * grid[i]
                                [j], dp[i-1][j][1] * grid[i][j]]
                else:
                    dp[i][j] = [max(dp[i-1][j][0] * grid[i][j], dp[i][j-1][0] * grid[i][j], dp[i-1][j][1] * grid[i][j], dp[i][j-1][1] * grid[i][j]),
                                min(dp[i-1][j][0] * grid[i][j], dp[i][j-1][0] * grid[i][j], dp[i-1][j][1] * grid[i][j], dp[i][j-1][1] * grid[i][j]),]
        res = dp[-1][-1][0]
        return res % mod if res >= 0 else -1


s = Solution()
print(s.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))  # -1
