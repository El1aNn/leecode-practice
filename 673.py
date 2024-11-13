from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        g = [1] * len(nums)

        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    dp[i] = max(dp[i], dp[j]+1)
            for j, y in enumerate(nums[:i]):
                if x > y:
                    if dp[i] == dp[j]+1:
                        g[i] += g[j]
                    elif dp[i] < dp[j]+1:
                        g[i] = g[j]
        max_len = max(dp) if dp else 0
        return sum(g[i] for i in range(len(nums)) if dp[i] == max_len)


s = Solution()
print(s.findNumberOfLIS([2, 2]))
