# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(list)
        m = 0
        len = 0
        for num in nums:
            if num not in d:
                d[num].append(1)
        for num in nums:
            if num - 1 not in d:
                len = 1
                while num + 1 in d:
                    len += 1
                    num += 1
            m = max(m, len)
        return m


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
