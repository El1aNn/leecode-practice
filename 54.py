# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        i, j = 0, 0
        temp = 0
        while len(ans) < m * n:
            ans.append(matrix[i][j])
            matrix[i][j] = 101


            if temp == 0:
                if j + 1 < m and (matrix[i][j + 1] <= 100):
                    j += 1
                    temp = 1
                else:
                    temp = 2
                    i += 1
            elif temp == 1:
                if j + 1 < m and (matrix[i][j + 1] <= 100):
                    j += 1
                else:
                    i += 1
                    temp = 2
            elif temp == 2:
                if i + 1 < n and matrix[i + 1][j] <= 100:
                    i += 1
                else:
                    j -= 1
                    temp = 3
            elif temp == 3:
                if j - 1 >= 0 and matrix[i][j - 1] <= 100:
                    j -= 1
                else:
                    i -= 1
                    temp = 4
            elif temp == 4:
                if i - 1 >= 0 and matrix[i - 1][j] <= 100:
                    i -= 1
                else:
                    j += 1
                    temp = 1
        return ans


s = Solution()
print(s.spiralOrder([[7], [9], [6]]))
