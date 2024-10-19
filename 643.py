from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        n = len(nums)
        m = -inf
        sum = 0
        for s in range(k):
            sum += nums[s]

        m = max(m, sum/k)
        while j < n-1:
            j += 1
            sum = sum - nums[i] + nums[j]
            m = max(m, sum/k)
            i += 1
        return m


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
