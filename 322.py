# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
import functools
from math import inf
from typing import List


class Solution:
    # def __init__(self):
    #     self.res = 0
    #
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     c = sorted(coins, reverse=True)
    #
    #     def backtrack(c, path, num, i):
    #         while self.res < amount and i < len(c):
    #             if c[i] + num < amount:
    #                 path.append(c[i])
    #                 self.res += c[i]
    #                 backtrack(c, path, num + c[i], i)
    #                 if self.res != amount and i < len(c):
    #                     temp = path.pop()
    #                     self.res -= temp
    #                     i += 1
    #             elif c[i] + num == amount:
    #                 path.append(c[i])
    #                 self.res += c[i]
    #             else:
    #                 backtrack(c, path, num, i + 1)
    #                 return path
    #         return path
    #
    #     temp = backtrack(c, [], 0, 0)
    #     if self.res == amount:
    #         return len(temp)
    #     else:
    #         return -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        #     dp = [amount + 1 for _ in range(amount + 1)]
        #     dp[0] = 0
        #     for coin in coins:
        #         for i in range(coin, amount + 1):
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        #     return -1 if dp[amount] == amount + 1 else dp[amount]
        # @functools.cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 0 if c == 0 else amount + 1
        #     if c < coins[i]: return dfs(i - 1, c)
        #     return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for c in range(coins[i], amount + 1):
                dp[c] = min(dp[c], dp[c - coins[i]] + 1)

        # ans = dfs(len(coins) - 1, amount)
        ans = dp[amount]
        return ans if ans < amount + 1 else -1


s = Solution()
print(s.coinChange([3, 2], 6))
