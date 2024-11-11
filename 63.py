from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n + 1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 or (i == 0 and j == 0):
                    continue
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        return dp[-1][-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
