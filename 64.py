# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] +=  grid[i][j-1] 
                elif j ==0:
                    grid[i][j] += grid[i-1][j]  
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
        return grid[-1][-1]