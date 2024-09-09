# 给你一个由
# '1'（陆地）和
# '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向 和/或 竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
import queue
from typing import List


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # def dfs(i, j, grid):
#         #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
#         #         return
#         #     grid[i][j] = '0'
#         #     dfs(i + 1, j, grid)
#         #     dfs(i - 1, j, grid)
#         #     dfs(i, j + 1, grid)
#         #     dfs(i, j - 1, grid)
#         #
#         # res = 0
#         # for i in range(len(grid)):
#         #     for j in range(len(grid[0])):
#         #         if grid[i][j] == '1':
#         #             dfs(i, j, grid)
#         #             res += 1
#         # return res
#         q = []
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     res += 1
#                     grid[i][j] = '0'
#                     q.append((i, j))
#                     while len(q) > 0:
#                         t = q.pop(0)
#                         x = t[0]
#                         y = t[1]
#                         if x - 1 >= 0 and grid[x - 1][y] == '1':
#                             q.append((x - 1, y))
#                             grid[x - 1][y] = '0'
#                         if x + 1 < len(grid) and grid[x + 1][y] == '1':
#                             q.append((x + 1, y))
#                             grid[x + 1][y] = '0'
#                         if y - 1 >= 0 and grid[x][y - 1] == '1':
#                             q.append((x, y - 1))
#                             grid[x][y - 1] = '0'
#                         if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
#                             q.append((x, y + 1))
#                             grid[x][y + 1] = '0'
#         return res

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        root = []  # 存储每个单元格的根坐标
        res = 0  # 记录岛屿的数量
        changed = set()  # 记录已经参与合并操作的单元格

        # 初始化根列表，使每个陆地单元格指向自身作为根
        for i in range(len(grid)):
            m = []
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    m.append((i, j))  # 如果是陆地，则根为自身坐标
                else:
                    m.append((-1, -1))  # 如果是水域，用 (-1, -1) 作为占位符
            root.append(m)

        # 辅助函数，找到给定单元格的根
        def find(i, j):
            if root[i][j] != (i, j):
                # 路径压缩：使当前单元格直接指向其根
                root[i][j] = find(root[i][j][0], root[i][j][1])
            return root[i][j]

        # 辅助函数，合并两个单元格，即连接它们
        def union(i1, j1, i2, j2):
            if grid[i1][j1] == '1' and grid[i2][j2] == '1' and root[i1][j1] != root[i2][j2]:
                # 将 (i2, j2) 单元格连接到 (i1, j1) 的根
                root[i2][j2] = find(i1, j1)

        # 遍历网格，对相邻的陆地单元格进行合并操作
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 检查上方单元格
                    if i - 1 >= 0 and grid[i - 1][j] == '1' and (i - 1, j) not in changed:
                        union(i, j, i - 1, j)
                        changed.add((i - 1, j))
                    # 检查下方单元格
                    if i + 1 < len(grid) and grid[i + 1][j] == '1' and (i + 1, j) not in changed:
                        union(i, j, i + 1, j)
                        changed.add((i + 1, j))
                    # 检查左侧单元格
                    if j - 1 >= 0 and grid[i][j - 1] == '1' and (i, j - 1) not in changed:
                        union(i, j, i, j - 1)
                        changed.add((i, j - 1))
                    # 检查右侧单元格
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == '1' and (i, j + 1) not in changed:
                        union(i, j, i, j + 1)
                        changed.add((i, j + 1))

        visited = set()  # 集合用于跟踪已经计数的岛屿
        # 计算唯一根的数量，它们代表岛屿的数量
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if root[i][j] != (-1, -1) and root[i][j] not in visited:
                    visited.add((i, j))
                    res += 1

        return res  # 返回岛屿的总数量


s = Solution()
print(s.numIslands(
    [["1", "0", "1", "1", "1"],
     ["1", "0", "1", "0", "1"],
     ["1", "1", "1", "0", "1"]]))
