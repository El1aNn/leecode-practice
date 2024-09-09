# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        N = []
        a = 0
        temp = -100000
        for i in nums:
            N.append(-i)
        heapq.heapify(N)
        for i in range(k - 1):
            heapq.heappop(N)
        return -heapq.heappop(N)


s = Solution()
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
