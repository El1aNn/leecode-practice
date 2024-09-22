# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        # dp = [False for _ in range(target + 1)]
        # dp[0] = True
        # for num in nums:
        #     for i in range(target, num - 1, -1):
        #         dp[i] = dp[i - num] or dp[i]
        # return dp[-1]
        # @cache
        # def dfs(i, l):
        #     if l == 0:
        #         return True
        #     if i < 0 :
        #         return False
        #     else:
        #         return dfs(i - 1, l) or dfs(i - 1, l - nums[i])
        # return dfs(len(nums) - 1, target)
        f = [[False] * (target + 1)for _ in range(len(nums) + 1)]
        for i, x in enumerate(nums):
            f[0][0] = True
            for j in range(target + 1):
                f[i + 1][j] = f[i][j] or (f[i][j - x] if j >= x else False)
        return f[-1][-1]
# 为什么要倒序？ 因为从前往后前面是i + 1 后面是 i，倒序是前面是i 后面是 i + 1，这样就能保证i + 1的状态能用到i的状态


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
