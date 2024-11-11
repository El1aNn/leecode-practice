from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp1 = [1] * n
        dp2 = [1] * n

        # 计算每个位置的最长递增子序列长度
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)

        # 计算每个位置的最长递减子序列长度
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)

        # 计算最长山脉长度
        res = 0
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                res = max(res, dp1[i] + dp2[i] - 1)

        return n - res


s = Solution()
print(s.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
