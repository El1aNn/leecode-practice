# 给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为 nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。
#
# 请你返回老师创建的小组能得到的最大实力值为多少。
from cmath import inf
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, pre_max)
            cur_min = min(pre_max * num, pre_min * num, pre_min)
            pre_max = cur_max
            pre_min = cur_min
        return pre_max


s = Solution()
print(s.maxStrength([0, -1]))
