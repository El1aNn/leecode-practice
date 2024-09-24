from typing import List
from functools import lru_cache


def coinChange(coins: List[int], amount: int) -> int:
    global a
    a = 1

    def f():

        a = 0
    f()
    return a


print(coinChange([186, 419, 83, 408], 6249))

# class Solution:

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         a = 1

#         def f():
#             nonlocal a
#             a = 0
#         f()
#         return a


# s = Solution()
# print(s.coinChange([186, 419, 83, 408], 6249))
