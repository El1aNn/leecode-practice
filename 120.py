from typing import List

from numpy import inf


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [inf for _ in range(n + 1)]
        dp[1] = triangle[0][0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                dp[j + 1] = min(dp[j + 1], dp[j]) + triangle[i][j]
        return min(dp)


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
