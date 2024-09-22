# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        row = [0 for _ in range(n)]

        def check(x, y):
            for i in range(x):
                if abs(row[i] - y) == abs(i - x):
                    return False
            return True

        def dfs(c, left):
            if c == n:
                ans.append(['.' * r + 'Q' + '.' * (n - r - 1) for r in row])
                return
            for i in left:
                if check(c, i):
                    row[c] = i
                    dfs(c + 1, left - {i})

        dfs(0, set(range(n)))

        return ans


s = Solution()
print(s.solveNQueens(4))
# from typing import List
#
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         ans = []  # 用来存储所有合法的解
#         row = [0] * n  # 记录每行放置皇后的位置，row[i] 表示第 i 行皇后在第 row[i] 列
#
#         def check(x, y):
#             # 检查在第 x 行的 y 列放置皇后是否安全
#             for i in range(x):
#                 # 检查是否有皇后在同一列
#                 if row[i] == y:
#                     return False
#                 # 检查是否有皇后在对角线上（左上或右上对角线）
#                 if abs(row[i] - y) == abs(i - x):
#                     return False
#             return True
#
#         def dfs(c):
#             # 如果所有行都成功放置了皇后，生成棋盘并加入答案
#             if c == n:
#                 board = ["." * r + "Q" + "." * (n - r - 1) for r in row]
#                 ans.append(board)
#                 return
#
#             for i in range(n):
#                 if check(c, i):  # 如果当前列位置合法
#                     row[c] = i  # 放置皇后
#                     dfs(c + 1)  # 递归处理下一行
#
#         dfs(0)  # 从第 0 行开始进行深度优先搜索
#         return ans
