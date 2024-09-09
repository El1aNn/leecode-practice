# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # for num in nums:
        #     if num not in d:
        #         d[num] = 1
        #     else:
        #         return True
        # return False
        s = set(nums)
        if len(s) == len(nums):
            return False
        return True


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
