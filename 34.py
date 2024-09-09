# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findLast(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        first = findFirst(nums, target)
        last = findLast(nums, target)

        # Check if target is actually in the array
        if first <= last and 0 <= first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
