from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0 for _ in range(len(nums))]
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # return dp[-1]
        n = len(nums)

        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     res = max(dfs(i - 1), dfs(i - 2) + nums[i])  # 选或不选
        #     return res
        #
        # return dfs(n - 1)
        @cache
        # def dfs(i, steel):
        #     if i < 0: return 0
        #     if steel:
        #         return max(dfs(i - 2, 0) + nums[i], dfs(i - 2, 1) + nums[i])
        #     return max(dfs(i - 1, 1), dfs(i - 1, 0))
        #
        # return max(dfs(n - 1, 0), dfs(n - 1, 1))
        def dfs(i):
            if i < 0:
                return 0, 0
            rob = dfs(i - 2) + nums[i]
            rob_not = dfs(i - 1)
            return rob, rob_not

        return max(dfs(n - 1))
s = Solution()
print(s.rob([]))
