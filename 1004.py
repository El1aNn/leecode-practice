from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = k
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count -= 1
            while count < 0:
                if nums[left] == 0:
                    count += 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
