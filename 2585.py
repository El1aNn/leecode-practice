from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        m = len(types)

        dp = [[[0 for _ in range(target + 1)] for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for i in range(1, m + 1):
            count, mark = types[i - 1]
            for j in range(i + 1):
                for k in range(target + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j > 0 and k >= mark:
                        dp[i][j][k] = (dp[i][j][k] + dp[i][j - 1][k - mark]) % mod

        return dp[m][m][target]



s = Solution()
print(s.waysToReachTarget(6, [[6, 1], [3, 2], [2, 3]]))
