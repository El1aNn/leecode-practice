# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = [float('inf')] * len(nums)
        # dp[0] = 0
        # if len(nums) == 1:
        #     return 0
        # for i in range(0, len(nums)):
        #     for j in range(1, nums[i] + 1):
        #         if i + j < len(nums):
        #             dp[i + j] = min(dp[i + j], dp[i] + 1)
        #             if dp[-1] != float('inf'):
        #                 return dp[-1]

        max_dist, step, end = 0, 0, 0
        for i in range(len(nums)-1):
            if i <= max_dist:
                max_dist = max(max_dist, i + nums[i])
                if i == end:
                    step += 1
                    end = max_dist
        return step


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
