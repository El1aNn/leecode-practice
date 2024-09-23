# 给你一个二维整数数组 ranges ，其中 ranges[i] = [starti, endi] 表示 starti 到 endi 之间（包括二者）的所有整数都包含在第 i 个区间中。

# 你需要将 ranges 分成 两个 组（可以为空），满足：

# 每个区间只属于一个组。
# 两个有 交集 的区间必须在 同一个 组内。
# 如果两个区间有至少 一个 公共整数，那么这两个区间是 有交集 的。

# 比方说，区间 [1, 3] 和 [2, 5] 有交集，因为 2 和 3 在两个区间中都被包含。
# 请你返回将 ranges 划分成两个组的 总方案数 。由于答案可能很大，将它对 109 + 7 取余 后返回。
from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        ans = []
        for range in ranges:
            if not ans or range[0] > ans[-1][1]:
                ans.append(range)
            else:
                ans[-1][1] = max(ans[-1][1], range[1])
        length = len(ans)
        return 2 ** length % (10**9 + 7)
