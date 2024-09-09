# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]:
                temp = height[i]
                i += 1
                while height[i] < temp:
                    i += 1
            else:
                temp = height[j]
                j -= 1
                while height[j] < temp:
                    j -= 1
            m = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, m)

        return maxArea


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
