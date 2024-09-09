from typing import List
from functools import lru_cache


class Solution:
    def __init__(self):
        self.res = 0

    def coinChange(self, coins: List[int], amount: int) -> int:
        c = sorted(coins, reverse=True)

        @lru_cache(amount)
        def backtrack(num, i):
            if num == amount:
                self.res = amount
                return 0

            if num < amount and i < len(c):
                take = 1 + backtrack(num + c[i], i)
                not_take = backtrack(num, i + 1)
                if not_take is not None:
                    return min(take, not_take)
                else:
                    return take

        result = backtrack(0, 0)
        if self.res == amount:
            return result
        else:
            return -1


s = Solution()
print(s.coinChange([186, 419, 83, 408], 6249))
