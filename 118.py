# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        path = []
        for i in range(numRows):
            path.append(1)
            if i > 1:
                for j in range(i - 1, 0, -1):
                    path[j] = path[j] + path[j - 1]
            res.append(path.copy())
        return res


s = Solution()
print(s.generate(4))
