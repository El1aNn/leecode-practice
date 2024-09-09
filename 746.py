# 给你一个整数数组cost ，其中cost[i]是从楼梯第i个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 你可以选择从下标为0或下标为1的台阶开始爬楼梯。请你计算并返回达到楼梯顶部的最低花费。
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        d[0] = d[1] = 0
        for i in range(2, len(cost) + 1):
            d[i] = min(d[i - 1] + cost[i - 1], d[i - 2] + cost[i - 2])
        return d[len(cost)]
