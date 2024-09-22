# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        s = sum(nums)
        target = s // k
        nums.sort(reverse=True)
        cur = [0] * k
        def backtrack(i):
            if i == len(nums):
                return True
            if nums[i] > target:
                return False
            for j in range(k):
                if j and cur[j] == cur[j - 1]:
                    continue
                if cur[j] + nums[i] <= target:
                    cur[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    cur[j] -= nums[i]
            return False
        return backtrack(0)

s = Solution()
print(s.canPartitionKSubsets([80,5,35,60,12,12,12,3,6,10,20,10], 3))
