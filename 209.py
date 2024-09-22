# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其总和大于等于 target 的长度最小的连续子数组
#
#  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 1000000000
        count = 0
        n = len(nums)
        i = 0
        j = 0
        sum = 0

        # while 1:
        sum += nums[0]
        if sum >= target:
            ans = 1
            # break
        else:
            while j < i or i == 0:
                while sum >= target:
                    sum -= nums[j]
                    j += 1
                    if sum >= target:
                        ans = min(ans, i - j + 1)
                        count = 1

                while sum < target and i + 1 < n:
                    sum += nums[i + 1]
                    i += 1
                if sum >= target:
                    count = 1
                    ans = min(ans, i - j + 1)
                if sum < target and i + 1 == n:
                    break
        return ans * count


s = Solution()
print(s.minSubArrayLen(15, [1, 2, 3, 4, 5]))
