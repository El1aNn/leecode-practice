# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchPos(nums: List[int], target: int) -> int:
            s = 0
            b = len(nums) - 1
            while s <= b:
                m = (s + b) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    s = m + 1
                else:
                    b = m - 1
            return s - 1

        def searchBool(nums: List[int], target: int) -> bool:
            s = 0
            b = len(nums) - 1
            while s <= b:
                m = (s + b) // 2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    s = m + 1
                else:
                    b = m - 1
            return False

        l0 = []
        for i in range(len(matrix)):
            l0.append(matrix[i][0])

        pos = searchPos(l0, target)

        return searchBool(matrix[pos], target)


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 15))

