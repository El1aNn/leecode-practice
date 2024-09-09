# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sets = set(nums)
        n = len(nums)
        for _ in sets:
            cnts = nums.count(_)
            if cnts > n // 2:
                return _


s = Solution()
print(s.majorityElement([2, 2, 3]))
