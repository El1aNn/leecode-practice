# 给定一个包含n + 1个整数的数组nums ，其数字都在[1, n]范围内（包括1和n），可知至少存在一个重复的整数。
# 假设nums只有一个重复的整数 ，返回这个重复的数 。
#
# 你设计的解决方案必须不修改数组nums且只用常量级O(1)的额外空间。
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res1 = []
        res2 = []

        def find(x):
            return nums[x]

        def dfind(x):
            return find(find(x))

        x1 = find(nums[0])
        x2 = dfind(nums[0])
        while x1 != x2:
            x1 = find(x1)
            x2 = dfind(x2)
        x2 = nums[0]
        while x1 != x2:
            x1 = find(x1)
            x2 = find(x2)
        return x2


S = Solution()
print(S.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
