# 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。

# 找出 A 中的坡的最大宽度，如果不存在，返回 0 。
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [0]
        ans = 0
        for i in range(1, n):
            if nums[stack[-1]] >= nums[i]:
                stack.append(i)
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i - stack.pop())
        return ans


s = Solution()
print(s.maxWidthRamp([6, 0, 8, 2, 1, 5]))  # 4
