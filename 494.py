# 给你一个非负整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
from typing import List

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         total = sum(nums)
#         if (total + target) % 2 != 0: return 0
#         if abs(target) > total: return 0
#         pos = (total + target) // 2
#         neg = (total - target) // 2
#         t = min(pos, neg)
#         dp = [0 for _ in range(t + 1)]
#         dp[0] = 1
#         for num in nums:
#             for i in range(t, num - 1, -1):
#                 dp[i] += dp[i - num]
#
#         return dp[-1]
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        t = (total + target) // 2  # 需要寻找的子集和

        def backtrack(index: int, current_sum: int) -> int:
            if current_sum == t:  # 找到一个符合条件的组合
                return 1
            if index >= len(nums) or current_sum > t:  # 超出范围或当前和超出目标
                return 0

            # 选择当前元素
            include = backtrack(index + 1, current_sum + nums[index])
            # 不选择当前元素
            exclude = backtrack(index + 1, current_sum)

            return include + exclude

        return backtrack(0, 0)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
