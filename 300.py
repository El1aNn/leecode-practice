# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列。
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pos = [nums[0]]
        for x in nums:
            p = bisect_left(pos, x)
            if p < len(pos):
                pos[p] = x
            else:
                pos.append(x)
        return len(pos)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
