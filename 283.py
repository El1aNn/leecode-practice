from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = 0
        i = 0
        while (1):
            if nums[i] == 0:
                nums.pop(i)
                m += 1
                i -= 1
            i += 1
            if (i == n - m):
                break
        for i in range(m):
            nums.append(0)
        return nums

    def moveZeroes1(self, nums: List[int]) -> None:
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] == 0:
                continue
            nums[index] = nums[i]
            index += 1
        for i in range(index, n):
            nums[i] = 0
        return nums


S = Solution()
print(S.moveZeroes1([0, 1, 0, 3, 12]))
