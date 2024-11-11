from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return float('-inf')
        #     return max(dfs(i - 1, j - 1) + nums1[i] * nums2[j], dfs(i - 1, j), dfs(i, j - 1), nums1[i] * nums2[j])
        # return dfs(m - 1, n - 1)
        dp = [float('-inf')] * n
        for i in range(m):
            pre = float('-inf')
            for j in range(n):
                dp[j], pre = max(pre + nums1[i] * nums2[j],
                                 dp[j], dp[j - 1], nums1[i] * nums2[j]), dp[j]
        return dp[-1]