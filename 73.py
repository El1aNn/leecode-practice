# 给定一个mxn的矩阵，如果一个元素为0 ，则将其所在行和列的所有元素都设为0 。请使用原地算法。
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """

        n = len(matrix)
        m = len(matrix[0])
        di = {}
        dj = {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    di[i] = 0
                    dj[j] = 0
        for i in range(n):
            for j in range(m):
                if i in di or j in dj:
                    matrix[i][j] = 0

        return


s = Solution()
print(s.setZeroes([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]))
