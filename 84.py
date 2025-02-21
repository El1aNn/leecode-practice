from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调递增栈，遇到一个较小的，可以算出前一个面积。宽需再次获取栈顶元素
        heights = [0] + heights + [0]

        stack = []
        ans = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                # 对于重复元素，会多次求面积，最后会算到最大面积
                # [9,8,7,7,7,7,6]. 6这里会分别与前面四个7算出最大面积
                dh = heights[stack.pop()]
                dw = i - stack[-1] - 1
                ans = max(ans, dh * dw)

            stack.append(i)

        return ans


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
