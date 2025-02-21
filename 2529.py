from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] == 0 and nums[-1] == 0:
            return 0
        n = len(nums)
        left, right = 0, len(nums) - 1
        target = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        ans = left
        if nums[-1] == 0:
            return left
        if left == -1 or left == n:
            return n
        while  nums[left] == target:
            left += 1

        ans = max(ans, len(nums) - left)
        return ans


s = Solution()
print(s.maximumCount([0, 0, 3, 4]))
