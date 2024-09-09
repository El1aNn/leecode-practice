# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
# BFS
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minute = [[-1 for _ in range(m)] for _ in range(n)]
        q = []
        num = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    minute[i][j] = 0
                    q.append((i, j))
                if grid[i][j] == 1:
                    num += 1
        if not q:
            return -1 if num else 0
        while q:
            (x, y) = q.pop(0)
            if x - 1 >= 0 and grid[x - 1][y] == 1:
                minute[x - 1][y] = minute[x][y] + 1
                q.append((x - 1, y))
                grid[x - 1][y] = 2
                num -= 1
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                minute[x][y - 1] = minute[x][y] + 1
                q.append((x, y - 1))
                grid[x][y - 1] = 2
                num -= 1
            if x + 1 < n and grid[x + 1][y] == 1:
                minute[x + 1][y] = minute[x][y] + 1
                q.append((x + 1, y))
                grid[x + 1][y] = 2
                num -= 1
            if y + 1 < m and grid[x][y + 1] == 1:
                minute[x][y + 1] = minute[x][y] + 1
                q.append((x, y + 1))
                grid[x][y + 1] = 2
                num -= 1

        return -1 if num else max(max(row) for row in minute)


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
