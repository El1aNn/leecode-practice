# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # s = 0
        # b = len(nums) - 1
        # while s <= b:
        #     if target == nums[0]:
        #         return 0
        #     elif target == nums[b]:
        #         return b
        #     else:
        #         m = (s + b) // 2
        #         if nums[m] == target:
        #             return m
        #         elif nums[m] < target:
        #             s = m + 1
        #         else:
        #             b = m - 1
        # return -1

        # s = Solution()
        # print(s.search([12], 12))
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
