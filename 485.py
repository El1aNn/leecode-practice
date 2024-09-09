from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = len(nums)
        m = 0
        max1 = 0
        for i in range(a):
            b = nums.pop()
            if b == 1:
                m += 1
            else:
                if m > max1:
                    max1 = m
                m = 0

        return max(m, max1)

m = Solution()
b = m.findMaxConsecutiveOnes([1, 1, 0, 1])
print(b)
bc= m.findMaxConsecutiveOnes([1, 1, 0, 1])