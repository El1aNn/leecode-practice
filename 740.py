# 给你一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums.sort()
        nums = list(set(nums))

        def dfs(n):
            if n <= 0:
                return 0
            return max(dfs(n - 1), dfs(n - 2) + cnt[n] * n)
        return dfs(max(nums))
