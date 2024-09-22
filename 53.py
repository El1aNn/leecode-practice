# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组
# 是数组中的一个连续部分。
from typing import List

from typing import List

from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #
    #     mid = len(nums) // 2
    #     left_max = self.max_subarray(nums[:mid])
    #     right_max = self.max_subarray(nums[mid:])
    #     cross_max = self.max_crossing_subarray(nums, mid)
    #
    #     return max(left_max, right_max, cross_max)
    #
    # def max_subarray(self, nums: List[int]) -> int:
    #     if not nums:
    #         return float('-inf')
    #
    #     mid = len(nums) // 2
    #
    #     left_max = self.max_subarray(nums[:mid])
    #     right_max = self.max_subarray(nums[mid:])
    #
    #     left_sum = float('-inf')
    #     right_sum = float('-inf')
    #     current_sum = 0
    #
    #     for i in range(mid - 1, -1, -1):
    #         current_sum += nums[i]
    #         left_sum = max(left_sum, current_sum)
    #
    #     current_sum = 0
    #     for i in range(mid, len(nums)):
    #         current_sum += nums[i]
    #         right_sum = max(right_sum, current_sum)
    #
    #     return max(left_max, right_max, left_sum + right_sum)
    #
    # def max_crossing_subarray(self, nums: List[int], mid: int) -> int:
    #     left_sum = float('-inf')
    #     right_sum = float('-inf')
    #     current_sum = 0
    #
    #     for i in range(mid - 1, -1, -1):
    #         current_sum += nums[i]
    #         left_sum = max(left_sum, current_sum)
    #
    #     current_sum = 0
    #     for i in range(mid, len(nums)):
    #         current_sum += nums[i]
    #         right_sum = max(right_sum, current_sum)
    #
    #     return left_sum + right_sum

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            dp[i + 1] = max(dp[i] + num, num)

        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     return max(dfs(i - 1) + nums[i], nums[i], 0)

        res = max(dp[:])
        return res


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans = nums[0]
#         m = nums[0]
#         i, j = 0, 0
#         new = 0
#         if max(nums) <= 0:
#             return max(nums)
#         else:
#             while i < len(nums):
#                 while (nums[i] <= 0 or i == 0) and new <= 0:
#                     i += 1
#                     m += nums[i]
#                     new += nums[i]
#                     if new > 0 or j == 0:
#                         ans = max(ans, m)
#
#                 while j < i:
#                     m -= nums[j]
#                     ans = max(ans, m)
#                     j += 1
#                     if i == j:
#                         i += 1
#                         m += nums[i]
#                         new += nums[i]
#                         break
#
#         return ans


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         return 0

#
# s = Solution()
# print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
