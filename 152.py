# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续
# 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for i in range(1, n):
            cur_max = max(pre_min * nums[i], pre_max * nums[i], nums[i])
            cur_min = min(pre_min * nums[i], pre_max * nums[i], nums[i])
            dp[i] = max(nums[i], cur_max)
            pre_max = cur_max
            pre_min = cur_min

        return max(dp)


from typing import List

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         pre_max = nums[0]
#         pre_min = nums[0]
#         max_product = nums[0]
#
#         for i in range(1, len(nums)):
#             # 当 nums[i] 为负数时，pre_max 和 pre_min 需要交换
#             if nums[i] < 0:
#                 pre_max, pre_min = pre_min, pre_max
#
#             pre_max = max(nums[i], pre_max * nums[i])
#             pre_min = min(nums[i], pre_min * nums[i])
#
#             max_product = max(max_product, pre_max)
#
#         return max_product


s = Solution()

print(s.maxProduct([-2, -4]))
