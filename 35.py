# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # # if len(nums) == 0:
        # #     return 0
        # #
        # # if len(nums) == 1:
        # #     if target <= nums[0]:
        # #         return 0
        # #     else:
        # #         return 1
        # #
        # s = 0
        # b = len(nums) - 1

        # while s <= b:
        #     # if target == nums[0]:
        #     #     return 0
        #     # elif target == nums[b]:
        #     #     return b
        #     # else:
        #     m = (s + b) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         s = m + 1
        #     else:
        #         b = m - 1
        # return s
        left, right = 0, len(nums) - 1  # []
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:  # [left, mid - 1]
                right = mid - 1
            else:
                left = mid + 1  # [mid + 1, right]
        return left


s = Solution()
print(s.searchInsert([1, 3, 5, 6, 8], 4))
