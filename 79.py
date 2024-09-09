# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(board)
        m = len(board[0])
        l = len(word)
        if l > m * n:
            return False

        board_count = Counter([board[i][j] for i in range(n) for j in range(m)])
        word_count = Counter(word)
        for char in word_count:
            if word_count[char] > board_count[char]:
                return False

        def backtrack(x, y, num):
            if board[x][y] != word[num]:
                return False
            elif num == l - 1:
                return True
            else:
                temp = board[x][y]
                board[x][y] = '#'  # 用特殊字符标记已访问的节点

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if backtrack(nx, ny, num + 1):
                            return True
                board[x][y] = temp
                return False

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
        return False
