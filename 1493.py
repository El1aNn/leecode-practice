# 给你一个二进制数组 nums ，你需要从中删掉一个元素。

# 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

# 如果不存在这样的子数组，请返回 0 。
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # sum1 = 0
        # sum2 = 0
        # for i in range(n):
        #     if nums[i] == 1:
        #         sum1 += 1
        #     else:
        #         sum2 = sum1
        #         sum1 = 0
        #     ans = max(ans, sum1 + sum2)
        # return ans - 1 if ans == n else ans
        ans = 0
        n = len(nums)
        left = 0
        d = {}
        for i in range(n):
            if nums[i] == 0:
                if d:
                    left = d[nums[i]] + 1
                d[nums[i]] = i
            ans = max(ans, i - left)
        return ans if d else ans + 1


s = Solution()
print(s.longestSubarray([1, 1, 0, 1,]))
