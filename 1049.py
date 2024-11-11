# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
#
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
import functools
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # @functools.lru_cache(maxsize=None)
        # def dp(rem):
        #     if rem < 0:
        #         return -1
        #     if rem == 0:
        #         return 0
        #     res = -int(1e9)
        #     for i in stones:
        #         if rem - i >= 0:
        #             res = max(res, dp(rem - i) + i)
        #     return res if res > -1e9 else -1
        #
        # total_weight = sum(stones)
        # target = total_weight // 2
        # x = dp(target)
        # return total_weight - 2 * x
        # total = sum(stones)
        # target = total // 2
        # dp = [0] * (target + 1)
        # for stone in stones:
        #     for i in range(target, stone - 1, -1):
        #         dp[i] = max(dp[i], dp[i - stone] + stone)
        # return total - 2 * dp[-1]

        total = sum(stones)
        target = total // 2

        # @cache
        # def dfs(i, left):
        #     if i < 0:
        #         return 0
        #     if left < stones[i]:
        #         return dfs(i - 1, left)
        #     return max(dfs(i - 1, left - stones[i]), dfs(i - 1, left))

        # return total - 2 * dfs(len(stones) - 1, target)
        dp = [0 for i in range(target + 1)]
        for stone in stones:
            for i in range(target, stone - 1, -1):
                dp[i] = max(dp[i], dp[i - stone])
        return total - 2 * dp[-1]


S = Solution()
print(S.lastStoneWeightII([31, 26, 33, 21, 40]))
