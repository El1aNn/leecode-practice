# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # if len(nums) == 2:
        #     if nums[0] > nums[1]:
        #         return 0
        #     else:
        #         return 1

        b = len(nums) - 1
        s = 0
        m = 0
        while s <= b:
            if nums[1] < nums[0]:
                return 0
            elif nums[b - 1] < nums[b]:
                return b
            else:
                m = (s + b) // 2
                if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                    return m
                elif nums[m] < nums[m + 1]:
                    s = m + 1
                else:
                    b = m - 1

        return m

    def findPeakElement1(self, A: List[int]) -> int:
        L, R = 0, len(A) - 1
        while L < R:
            M = (L + R) // 2
            if A[M] >= A[M + 1]:
                R = M
            else:
                L = M + 1
        return L


s = Solution()
print(s.findPeakElement([3, 2]))
