# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

# 子数组 是数组的一段连续部分。
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(nums, goal):
            n = len(nums)
            left = 0
            ans = 0
            for right in range(n):
                goal -= nums[right]
                while goal <= 0 and left <= right:
                    goal += nums[left]
                    left += 1
                ans += left
            return ans
        return atMost(nums, goal) - atMost(nums, goal+1)


s = Solution()
print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
