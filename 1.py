# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if target - nums[i] == nums[i]:
                    return [d[nums[i]], i]
        for i in range(len(nums)):
            if target - nums[i] in d and (target - nums[i]) != nums[i]:

                return [i, d[target - nums[i]]]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in d:
#                 return [d[complement], i]
#             d[num] = i
s = Solution()
print(s.twoSum([3, 2, 4], 6))
