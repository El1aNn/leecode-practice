from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


S = Solution()

print(S.removeElement([3, 2, 2, 3], 3))
