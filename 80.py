from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        left = 0
        for i, x in enumerate(nums):
            if i > 0 and nums[i] != nums[i - 1]:
                k = 2
            k -= 1
            if k >= 0:
                nums[left] = x
                left += 1
        return nums[:left]
    
s = Solution()
print(s.removeDuplicates([1, 1, 2]))  # 5

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2  # 允许每个元素最多出现两次
        left = 0
        
        for i in range(n):
            # 如果当前元素和前一个元素不同，重置 k 为 2
            if i > 0 and nums[i] != nums[i - 1]:
                k = 2
                
            # 如果当前元素的重复次数未超过 2，则可以保留
            if k > 0:
                nums[left] = nums[i]
                left += 1
                k -= 1
        
        return left