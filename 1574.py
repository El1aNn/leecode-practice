# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

# 一个子数组指的是原数组中连续的一个子序列。

# 请你返回满足题目要求的最短子数组的长度
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = n - 1
        left, right = 0, n - 1
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return n - 1
        left = 0
        ans = min(right - left, ans)
        while right < n:
            while left < n and arr[left] <= arr[right]:
                ans = min(ans, right - left - 1)
                left += 1
            right += 1
        return ans


s = Solution()
print(s.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]))  # 3
