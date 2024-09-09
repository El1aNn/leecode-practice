# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
from collections import deque
from typing import List


# class Solution:

# def findCircleNum(self, isConnected: List[List[int]]) -> int:
# 查并集
#     res = 0
#     root = [-1] * len(isConnected)
#     for i in range(len(isConnected)):
#         root[i] = i
#
#     def find(x):
#         if x == root[x]:
#             return x
#         else:
#             return find(root[x])
#
#     def union(x, y):
#         x_root, y_root = find(x), find(y)
#         if isConnected[x][y] == 1 and x_root != y_root:
#             root[y_root] = x_root
#
#     for i in range(len(isConnected)):
#         for j in range(i + 1, len(isConnected)):
#             union(i, j)
#     res = sum(root[i] == i for i in range(len(isConnected)))
#     return res


# class Solution: dfs
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         res = 0
#         visited = set()
#
#         def dfs(i):
#             for j in range(len(isConnected)):
#                 if isConnected[i][j] == 1 and j not in visited:
#                     visited.add(j)
#                     dfs(j)
#
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 dfs(i)
#                 res += 1
#
#         return res

class Solution:
    # bfs
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        queue = deque()

        def bfs(queue, i):
            queue.append(i)
            while queue:
                x = queue.popleft()
                for y in range(len(isConnected)):
                    if isConnected[x][y] == 1 and y not in visited:
                        queue.append(y)
                        visited.add(y)

        for i in range(len(isConnected)):
            if i not in visited:
                bfs(queue, i)
                res += 1

        return res


s = Solution()
print(s.findCircleNum([[1, 0, 0, 1],
                       [0, 1, 1, 0],
                       [0, 1, 1, 1],
                       [1, 0, 1, 1]]))
