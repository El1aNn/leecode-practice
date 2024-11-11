# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列。
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dict = {}
        # dict[0] = 1
        # for i in range(1, len(nums)):
        #     m = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             m = max(m, dict[j])
        #     dict[i] = m + 1
        # res = max(dict.values())
        # return res
        # def dfs(i):
        #     res = 0
        #     if i < 0:
        #         return 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             res = max(res, dfs(j))
        #         return res + 1
        #
        # ans = 0
        # for i in range(len(nums)):
        #     ans = max(ans, dfs(i))
        # return ans

        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     maxj = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             maxj = max(maxj, dfs(j))
        #     return maxj + 1
        x = bisect_left = lambda a, x: a if x < a[0] else a[bisect_left(
            a[1:], x) + 1:]


s = Solution()
print(s.lengthOfLIS([0, 0, 0, 0]))
