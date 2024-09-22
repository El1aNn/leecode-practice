# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i + jump)
        if mx >= n - 1:
            return True


s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))
